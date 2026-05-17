"""
Scratch 3.0 项目构建器
提供高层 API 来创建完整的 Scratch 项目
"""

import uuid
import json
import os


def _new_id():
    return uuid.uuid4().hex[:16]


class ScratchProject:
    """Scratch 项目构建器"""

    def __init__(self):
        self.targets = []
        self.monitors = []
        self.extensions = []
        self._stage = None
        self._sprites = []

    def create_stage(self, name="Stage"):
        """创建舞台"""
        self._stage = {
            "isStage": True,
            "name": name,
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
        self.targets.append(self._stage)
        return self._stage

    def create_sprite(self, name, x=0, y=0, size=100, direction=90):
        """创建角色"""
        sprite = {
            "isStage": False,
            "name": name,
            "variables": {},
            "lists": {},
            "broadcasts": {},
            "blocks": {},
            "comments": {},
            "currentCostume": 0,
            "costumes": [],
            "sounds": [],
            "volume": 100,
            "layerOrder": len(self.targets),
            "visible": True,
            "x": x,
            "y": y,
            "size": size,
            "direction": direction,
            "draggable": False,
            "rotationStyle": "all around"
        }
        self._sprites.append(sprite)
        self.targets.append(sprite)
        return sprite

    def add_variable(self, target, var_name, initial_value=0):
        """添加变量"""
        var_id = _new_id()
        target["variables"][var_id] = [var_name, initial_value]
        return var_id

    def add_list(self, target, list_name, initial_items=None):
        """添加列表"""
        list_id = _new_id()
        target["lists"][list_id] = [list_name, initial_items or []]
        return list_id

    def add_broadcast(self, target, msg_name):
        """添加广播消息"""
        msg_id = _new_id()
        target["broadcasts"][msg_id] = msg_name
        return msg_id

    def add_costume(self, target, name, data_format="svg",
                   rotation_center_x=48, rotation_center_y=50,
                   bitmap_resolution=1, asset_id=None, md5ext=None):
        """添加造型"""
        costume = {
            "name": name,
            "bitmapResolution": bitmap_resolution,
            "dataFormat": data_format,
            "rotationCenterX": rotation_center_x,
            "rotationCenterY": rotation_center_y
        }
        if asset_id:
            costume["assetId"] = asset_id
        if md5ext:
            costume["md5ext"] = md5ext
        target["costumes"].append(costume)
        return costume

    def add_sound(self, target, name, data_format="wav",
                  rate=48000, sample_count=0, asset_id=None, md5ext=None):
        """添加声音"""
        sound = {
            "name": name,
            "dataFormat": data_format,
            "rate": rate,
            "sampleCount": sample_count
        }
        if asset_id:
            sound["assetId"] = asset_id
        if md5ext:
            sound["md5ext"] = md5ext
        target["sounds"].append(sound)
        return sound

    def add_block(self, target, opcode, inputs=None, fields=None,
                  next_block=None, parent=None, top_level=False, x=0, y=0):
        """添加积木块"""
        block_id = _new_id()
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
        target["blocks"][block_id] = block
        return block_id

    def add_blocks_from_chain(self, target, blocks_list):
        """
        从列表中添加连接的积木块链。

        blocks_list: [(opcode, inputs, fields), ...]
        返回第一个积木块的 ID
        """
        prev_id = None
        first_id = None

        for i, (opcode, inputs, fields) in enumerate(blocks_list):
            block_id = self.add_block(
                target,
                opcode=opcode,
                inputs=inputs or {},
                fields=fields or {},
                next_block=None,
                parent=prev_id,
                top_level=(i == 0),
                x=0,
                y=i * 100
            )
            if prev_id:
                target["blocks"][prev_id]["next"] = block_id
            if i == 0:
                first_id = block_id
            prev_id = block_id

        return first_id

    def add_extension(self, ext_name):
        """添加扩展"""
        if ext_name not in self.extensions:
            self.extensions.append(ext_name)

    def to_dict(self):
        """导出为 project.json 字典"""
        return {
            "targets": self.targets,
            "monitors": self.monitors,
            "extensions": self.extensions,
            "meta": {
                "semver": "3.0.0",
                "vm": "0.2.0",
                "agent": ""
            }
        }

    def save_json(self, filepath):
        """保存 project.json 到文件"""
        os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else '.', exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=2)
        return filepath

    def validate(self):
        """验证项目完整性"""
        issues = []
        if not self._stage:
            issues.append("缺少 Stage")
        if len(self.targets) < 2:
            issues.append("项目中没有角色（Sprite）")

        for target in self.targets:
            name = target.get("name", "unknown")
            if not target.get("costumes"):
                issues.append(f"{name}: 没有造型")
            if target.get("currentCostume", 0) >= len(target.get("costumes", [])):
                if target.get("costumes"):
                    issues.append(f"{name}: currentCostume 超出范围")

        return len(issues) == 0, issues


def quick_project(sprite_name="Sprite1"):
    """快速创建一个带默认背景和角色的项目"""
    proj = ScratchProject()

    # 创建舞台
    stage = proj.create_stage()
    proj.add_costume(stage, "空白背景", data_format="svg",
                     rotation_center_x=240, rotation_center_y=180)

    # 创建角色
    sprite = proj.create_sprite(sprite_name)
    proj.add_costume(sprite, "造型1", data_format="svg")

    return proj
