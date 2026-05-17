"""
Scratch 3.0 (.sb3) 工具函数
提供 .sb3 文件的打包、解包、创建和验证功能
"""

import zipfile
import json
import os
import uuid
import hashlib
import shutil


def generate_block_id():
    """生成一个唯一的积木块 ID"""
    return uuid.uuid4().hex[:16]


def unpack_sb3(sb3_path, output_dir=None):
    """
    将 .sb3 文件解压到目录。

    Args:
        sb3_path: .sb3 文件路径
        output_dir: 输出目录，默认为同名目录

    Returns:
        (project_dir, project_data) 元组
    """
    if output_dir is None:
        output_dir = sb3_path.replace('.sb3', '_unpacked')

    os.makedirs(output_dir, exist_ok=True)

    with zipfile.ZipFile(sb3_path, 'r') as z:
        z.extractall(output_dir)

    json_path = os.path.join(output_dir, 'project.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        project_data = json.load(f)

    return output_dir, project_data


def pack_sb3(project_dir, output_path):
    """
    将目录打包为 .sb3 文件。

    Args:
        project_dir: 项目目录（需包含 project.json）
        output_path: 输出的 .sb3 文件路径
    """
    # 验证 project.json 存在
    json_path = os.path.join(project_dir, 'project.json')
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"project.json not found in {project_dir}")

    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, dirs, files in os.walk(project_dir):
            for file in files:
                filepath = os.path.join(root, file)
                arcname = os.path.relpath(filepath, project_dir)
                z.write(filepath, arcname)

    return output_path


def create_empty_project():
    """
    创建一个空的 Scratch 3.0 项目结构。

    Returns:
        project_data (dict)
    """
    return {
        "targets": [
            {
                "isStage": True,
                "name": "Stage",
                "variables": {},
                "lists": {},
                "broadcasts": {},
                "blocks": {},
                "comments": {},
                "currentCostume": 0,
                "costumes": [],
                "sounds": [],
                "volume": 100,
                "layerOrder": 0,
                "tempo": 60,
                "videoTransparency": 50,
                "videoState": "on",
                "textToSpeechLanguage": None
            }
        ],
        "monitors": [],
        "extensions": [],
        "meta": {
            "semver": "3.0.0",
            "vm": "0.2.0",
            "agent": ""
        }
    }


def add_sprite(project_data, name, x=0, y=0, size=100, direction=90,
               costumes=None, sounds=None):
    """
    向项目中添加一个角色。

    Args:
        project_data: 项目数据字典
        name: 角色名称
        x, y: 初始坐标
        size: 大小百分比
        direction: 初始方向
        costumes: 造型列表 [{"name": "xxx", "svg_content": "..."}]
        sounds: 声音列表

    Returns:
        sprite 字典
    """
    sprite = {
        "isStage": False,
        "name": name,
        "variables": {},
        "lists": {},
        "broadcasts": {},
        "blocks": {},
        "comments": {},
        "currentCostume": 0,
        "costumes": costumes or [],
        "sounds": sounds or [],
        "volume": 100,
        "layerOrder": len(project_data["targets"]),
        "visible": True,
        "x": x,
        "y": y,
        "size": size,
        "direction": direction,
        "draggable": False,
        "rotationStyle": "all around"
    }
    project_data["targets"].append(sprite)
    return sprite


def add_backdrop(stage, name, svg_content=None):
    """
    向舞台添加背景。

    Args:
        stage: Stage target 字典
        name: 背景名称
        svg_content: SVG 内容字符串
    """
    costume = {
        "name": name,
        "bitmapResolution": 1,
        "dataFormat": "svg" if svg_content else "png",
        "rotationCenterX": 240,
        "rotationCenterY": 180
    }

    if svg_content:
        md5 = hashlib.md5(svg_content.encode('utf-8')).hexdigest()
        costume["assetId"] = md5
        costume["md5ext"] = f"{md5}.svg"

    stage["costumes"].append(costume)
    return costume


def create_block(opcode, inputs=None, fields=None, next_block=None,
                 parent=None, top_level=False, x=0, y=0):
    """
    创建一个积木块字典。

    Args:
        opcode: 积木块类型
        inputs: 输入字典
        fields: 字段字典
        next_block: 下一个积木块 ID
        parent: 父积木块 ID
        top_level: 是否为顶层积木块
        x, y: 坐标

    Returns:
        (block_id, block_dict) 元组
    """
    block_id = generate_block_id()
    block = {
        "opcode": opcode,
        "next": next_block,
        "parent": parent,
        "inputs": inputs or {},
        "fields": fields or {},
        "shadow": False,
        "topLevel": top_level,
        "x": x,
        "y": y
    }
    return block_id, block


def add_block_to_target(target, block_id, block_dict):
    """将积木块添加到目标（角色/舞台）"""
    target["blocks"][block_id] = block_dict


def create_simple_script(target, blocks_list):
    """
    将一系列积木块连接成脚本链。

    Args:
        target: target 字典
        blocks_list: [(opcode, inputs, fields), ...] 列表

    Returns:
        第一个积木块的 ID
    """
    prev_id = None
    first_id = None

    for i, (opcode, inputs, fields) in enumerate(blocks_list):
        block_id, block_dict = create_block(
            opcode=opcode,
            inputs=inputs or {},
            fields=fields or {},
            top_level=(i == 0),
            x=0,
            y=i * 100
        )

        if prev_id:
            target["blocks"][prev_id]["next"] = block_id
            block_dict["parent"] = prev_id

        target["blocks"][block_id] = block_dict

        if i == 0:
            first_id = block_id
        prev_id = block_id

    return first_id


def validate_project(project_data):
    """
    验证项目数据的基本完整性。

    Returns:
        (is_valid, issues) 元组
    """
    issues = []

    # 检查必需字段
    if "targets" not in project_data:
        issues.append("缺少 targets 字段")
    elif len(project_data["targets"]) == 0:
        issues.append("targets 为空")
    else:
        # 检查是否有舞台
        stages = [t for t in project_data["targets"] if t.get("isStage")]
        if len(stages) == 0:
            issues.append("缺少 Stage（舞台）")
        elif len(stages) > 1:
            issues.append("有多个 Stage（应只有一个）")

    # 检查 meta
    if "meta" not in project_data:
        issues.append("缺少 meta 字段")

    # 检查每个 target
    for i, target in enumerate(project_data.get("targets", [])):
        prefix = f"Target[{i}] ({target.get('name', 'unknown')})"
        if "blocks" not in target:
            issues.append(f"{prefix}: 缺少 blocks 字段")
        if "costumes" not in target:
            issues.append(f"{prefix}: 缺少 costumes 字段")
        if "currentCostume" in target and target["costumes"]:
            if target["currentCostume"] >= len(target["costumes"]):
                issues.append(f"{prefix}: currentCostume 超出 costumes 范围")

    return len(issues) == 0, issues


def create_project_directory(project_data, output_dir, media_files=None):
    """
    创建项目目录并写入 project.json。

    Args:
        project_data: 项目数据字典
        output_dir: 输出目录
        media_files: {filename: content_bytes} 媒体文件字典
    """
    os.makedirs(output_dir, exist_ok=True)

    # 写入 project.json
    json_path = os.path.join(output_dir, 'project.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(project_data, f, ensure_ascii=False, indent=2)

    # 写入媒体文件
    if media_files:
        for filename, content in media_files.items():
            filepath = os.path.join(output_dir, filename)
            if isinstance(content, str):
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
            else:
                with open(filepath, 'wb') as f:
                    f.write(content)

    return output_dir


# ===== 快捷积木块输入构造 =====

def num(value):
    """数字输入"""
    return [1, [4, str(value)]]


def str_input(value):
    """字符串输入"""
    return [1, [10, str(value)]]


def var_ref(variable_name, var_id):
    """变量引用"""
    return [1, [12, var_id, variable_name]]


def block_ref(block_id):
    """积木块引用"""
    return [2, block_id]


def block_ref_with_default(block_id, default):
    """带默认值的积木块引用"""
    return [3, block_id, [10, str(default)]]


def field_value(value):
    """简单字段值"""
    return [value, None]


def color_val(hex_color):
    """颜色值"""
    return [1, hex_color]


null = None


# ===== 示例和测试 =====

def create_demo_project():
    """
    创建一个演示项目：点击绿旗后角色移动并说话。
    用于测试 skill 功能。
    """
    project = create_empty_project()
    stage = project["targets"][0]

    # 添加简单背景（纯蓝色 SVG）
    blue_bg = '''<svg xmlns="http://www.w3.org/2000/svg" width="480" height="360">
  <rect width="480" height="360" fill="#0000FF"/>
</svg>'''
    add_backdrop(stage, "blue", blue_bg)

    # 添加简单角色
    cat_svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="96" height="100">
  <ellipse cx="48" cy="50" rx="40" ry="45" fill="#FFA500"/>
  <circle cx="35" cy="35" r="5" fill="#000"/>
  <circle cx="61" cy="35" r="5" fill="#000"/>
</svg>'''

    cat_md5 = hashlib.md5(cat_svg.encode('utf-8')).hexdigest()

    costumes = [{
        "name": "cat",
        "bitmapResolution": 1,
        "dataFormat": "svg",
        "assetId": cat_md5,
        "md5ext": f"{cat_md5}.svg",
        "rotationCenterX": 48,
        "rotationCenterY": 50
    }]

    sprite = add_sprite(project, "Sprite1", costumes=costumes)

    # 添加脚本：点击绿旗 → 说"你好" → 移动10步
    b1_id = generate_block_id()
    b2_id = generate_block_id()
    b3_id = generate_block_id()

    sprite["blocks"][b1_id] = {
        "opcode": "event_whenflagclicked",
        "next": b2_id,
        "parent": None,
        "inputs": {},
        "fields": {},
        "shadow": False,
        "topLevel": True,
        "x": 0,
        "y": 0
    }

    sprite["blocks"][b2_id] = {
        "opcode": "looks_say",
        "next": b3_id,
        "parent": b1_id,
        "inputs": {"MESSAGE": str_input("你好！")},
        "fields": {},
        "shadow": False,
        "topLevel": False,
        "x": 0,
        "y": 100
    }

    sprite["blocks"][b3_id] = {
        "opcode": "motion_movesteps",
        "next": None,
        "parent": b2_id,
        "inputs": {"STEPS": num(10)},
        "fields": {},
        "shadow": False,
        "topLevel": False,
        "x": 0,
        "y": 200
    }

    # 验证
    is_valid, issues = validate_project(project)
    if not is_valid:
        print(f"警告: 项目验证问题: {issues}")

    # 收集素材文件
    backdrop = stage["costumes"][0]
    media_files = {
        backdrop["md5ext"]: blue_bg,
        costumes[0]["md5ext"]: cat_svg
    }

    return project, media_files


if __name__ == "__main__":
    # 创建演示项目并打包
    project, media_files = create_demo_project()

    # 创建临时目录
    demo_dir = os.path.join(os.path.dirname(__file__), '..', 'demo_project')
    demo_dir = os.path.normpath(demo_dir)

    create_project_directory(project, demo_dir, media_files=media_files)
    print(f"项目已创建: {demo_dir}")

    # 打包为 .sb3
    sb3_path = demo_dir + '.sb3'
    pack_sb3(demo_dir, sb3_path)
    print(f"已打包: {sb3_path}")

    # 验证
    is_valid, issues = validate_project(project)
    print(f"验证结果: {'通过' if is_valid else '失败'}")
    if issues:
        for issue in issues:
            print(f"  - {issue}")
