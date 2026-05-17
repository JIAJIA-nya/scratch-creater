"""
Scratch 3.0 积木块构建器
提供便捷的积木块创建和连接功能
"""

import uuid


def gen_id():
    """生成唯一积木块 ID"""
    return uuid.uuid4().hex[:16]


class BlockBuilder:
    """积木块构建器，支持链式调用"""

    def __init__(self, opcode):
        self.block_id = gen_id()
        self.opcode = opcode
        self.inputs = {}
        self.fields = {}
        self.next_block = None
        self.parent = None
        self.top_level = False
        self.shadow = False
        self.x = 0
        self.y = 0

    def set_input(self, name, value):
        """设置输入值"""
        self.inputs[name] = value
        return self

    def set_field(self, name, value):
        """设置字段值"""
        self.fields[name] = value
        return self

    def set_position(self, x, y):
        """设置坐标"""
        self.x = x
        self.y = y
        return self

    def set_top_level(self, is_top=True):
        """设为顶层积木"""
        self.top_level = is_top
        return self

    def set_shadow(self, is_shadow=True):
        """设为阴影块"""
        self.shadow = is_shadow
        return self

    def connect_next(self, other_builder):
        """连接下一个积木块"""
        self.next_block = other_builder.block_id
        other_builder.parent = self.block_id
        return self

    def build(self):
        """构建积木块字典"""
        return self.block_id, {
            "opcode": self.opcode,
            "next": self.next_block,
            "parent": self.parent,
            "inputs": self.inputs,
            "fields": self.fields,
            "shadow": self.shadow,
            "topLevel": self.top_level,
            "x": self.x,
            "y": self.y
        }


class ScriptBuilder:
    """脚本构建器，管理多个积木块的连接"""

    def __init__(self):
        self.blocks = {}  # {block_id: block_dict}
        self.first_id = None
        self._prev_id = None

    def add(self, opcode, inputs=None, fields=None, is_top_level=False):
        """添加一个积木块到脚本末尾"""
        builder = BlockBuilder(opcode)
        builder.set_top_level(is_top_level)

        if inputs:
            for k, v in inputs.items():
                builder.set_input(k, v)
        if fields:
            for k, v in fields.items():
                builder.set_field(k, v)

        block_id, block_dict = builder.build()
        self.blocks[block_id] = block_dict

        if self._prev_id:
            self.blocks[self._prev_id]["next"] = block_id
            block_dict["parent"] = self._prev_id
        else:
            self.first_id = block_id

        self._prev_id = block_id
        return block_id

    def build(self):
        """返回所有积木块字典"""
        return self.blocks


# ===== 便捷输入构造函数 =====

def num(value):
    """数字输入"""
    return [1, [4, str(value)]]


def positive_int(value):
    """正整数输入"""
    return [1, [5, str(value)]]


def positive_num(value):
    """正数输入"""
    return [1, [6, str(value)]]


def integer(value):
    """整数输入"""
    return [1, [7, str(value)]]


def angle(value):
    """角度输入"""
    return [1, [8, str(value)]]


def string(value):
    """字符串输入"""
    return [1, [10, str(value)]]


def variable_ref(var_id, var_name):
    """变量引用"""
    return [1, [12, var_id, var_name]]


def block_ref(block_id):
    """积木块引用（reporter）"""
    return [2, block_id]


def block_ref_default(block_id, default):
    """带默认值的积木块引用"""
    return [3, block_id, [10, str(default)]]


def field_val(value):
    """字段值"""
    return [value, None]


def color_val(hex_color):
    """颜色值"""
    return [1, hex_color]


# ===== 便捷积木块创建 =====

def make_event_whenflagclicked():
    """当绿旗被点击"""
    return BlockBuilder("event_whenflagclicked").set_top_level(True)


def make_event_whenkeypressed(key):
    """当按下某键"""
    b = BlockBuilder("event_whenkeypressed").set_top_level(True)
    b.set_field("KEY_OPTION", [key, null])
    return b


def make_event_whenbroadcastreceived(msg_name, msg_id):
    """当接收到消息"""
    b = BlockBuilder("event_whenbroadcastreceived").set_top_level(True)
    b.set_field("BROADCAST_OPTION", [msg_name, msg_id])
    return b


def make_broadcast(msg_name, msg_id):
    """广播消息"""
    b = BlockBuilder("event_broadcast")
    b.set_input("BROADCAST_INPUT", [1, [11, msg_name, msg_id]])
    return b


def make_movesteps(steps):
    """移动 N 步"""
    b = BlockBuilder("motion_movesteps")
    b.set_input("STEPS", num(steps))
    return b


def make_turnright(degrees):
    """右转 N 度"""
    b = BlockBuilder("motion_turnright")
    b.set_input("DEGREES", num(degrees))
    return b


def make_turnleft(degrees):
    """左转 N 度"""
    b = BlockBuilder("motion_turnleft")
    b.set_input("DEGREES", num(degrees))
    return b


def make_gotoxy(x, y):
    """移动到 x, y"""
    b = BlockBuilder("motion_gotoxy")
    b.set_input("X", num(x))
    b.set_input("Y", num(y))
    return b


def make_glidesecstoxy(secs, x, y):
    """滑行 N 秒到 x, y"""
    b = BlockBuilder("motion_glidesecstoxy")
    b.set_input("SECS", num(secs))
    b.set_input("X", num(x))
    b.set_input("Y", num(y))
    return b


def make_pointindirection(direction):
    """面向方向"""
    b = BlockBuilder("motion_pointindirection")
    b.set_field("DIRECTION", [str(direction), null])
    return b


def make_pointtowards(target):
    """面向... (鼠标指针: _mouse_, 随机: _random_)"""
    b = BlockBuilder("motion_pointtowards")
    b.set_input("TOWARDS", [1, target])
    return b


def make_ifonedgebounce():
    """碰到边缘反弹"""
    return BlockBuilder("motion_ifonedgebounce")


def make_say(message):
    """说 ..."""
    b = BlockBuilder("looks_say")
    b.set_input("MESSAGE", string(message))
    return b


def make_sayforseconds(message, secs):
    """说 ... N 秒"""
    b = BlockBuilder("looks_sayforseconds")
    b.set_input("MESSAGE", string(message))
    b.set_input("SECS", num(secs))
    return b


def make_think(message):
    """想 ..."""
    b = BlockBuilder("looks_think")
    b.set_input("MESSAGE", string(message))
    return b


def make_show():
    """显示"""
    return BlockBuilder("looks_show")


def make_hide():
    """隐藏"""
    return BlockBuilder("looks_hide")


def make_nextcostume():
    """下一个造型"""
    return BlockBuilder("looks_nextcostume")


def make_nextbackdrop():
    """下一个背景"""
    return BlockBuilder("looks_nextbackdrop")


def make_switchbackdropto(backdrop_name):
    """切换背景为 ..."""
    b = BlockBuilder("looks_switchbackdropto")
    b.set_input("BACKDROP", [1, "backdrop_shadow"])
    # 需要额外的 shadow 块
    return b


def make_changesizeby(change):
    """大小增加 N"""
    b = BlockBuilder("looks_changesizeby")
    b.set_input("CHANGE", num(change))
    return b


def make_setsizeto(size):
    """大小设为 N%"""
    b = BlockBuilder("looks_setsizeto")
    b.set_input("SIZE", num(size))
    return b


def make_changeeffectby(effect, change):
    """将特效增加 N"""
    b = BlockBuilder("looks_changeeffectby")
    b.set_field("EFFECT", [effect, null])
    b.set_input("CHANGE", num(change))
    return b


def make_seteffectto(effect, value):
    """将特效设为 N"""
    b = BlockBuilder("looks_seteffectto")
    b.set_field("EFFECT", [effect, null])
    b.set_input("VALUE", num(value))
    return b


def make_cleargraphiceffects():
    """清除图形特效"""
    return BlockBuilder("looks_cleargraphiceffects")


def make_gotofront():
    """移到最前面"""
    b = BlockBuilder("looks_gotofrontback")
    b.set_field("FRONT_BACK", ["front", null])
    return b


def make_gotoback():
    """移到最后面"""
    b = BlockBuilder("looks_gotofrontback")
    b.set_field("FRONT_BACK", ["back", null])
    return b


def make_wait(secs):
    """等待 N 秒"""
    b = BlockBuilder("control_wait")
    b.set_input("DURATION", [1, [5, str(secs)]])
    return b


def make_repeat(times):
    """重复 N 次"""
    b = BlockBuilder("control_repeat")
    b.set_input("TIMES", [1, [6, str(times)]])
    return b


def make_forever():
    """重复执行"""
    return BlockBuilder("control_forever")


def make_if():
    """如果 ... 那么"""
    return BlockBuilder("control_if")


def make_if_else():
    """如果 ... 那么 ... 否则"""
    return BlockBuilder("control_if_else")


def make_wait_until():
    """等待 ..."""
    return BlockBuilder("control_wait_until")


def make_repeat_until():
    """重复执行直到 ..."""
    return BlockBuilder("control_repeat_until")


def make_stop_all():
    """停止全部脚本"""
    b = BlockBuilder("control_stop")
    b.set_field("STOP_OPTION", ["all", null])
    return b


def make_stop_this():
    """停止这个脚本"""
    b = BlockBuilder("control_stop")
    b.set_field("STOP_OPTION", ["this script", null])
    return b


def make_start_as_clone():
    """当作为克隆体启动时"""
    return BlockBuilder("control_start_as_clone").set_top_level(True)


def make_create_clone_of(target):
    """克隆 ..."""
    b = BlockBuilder("control_create_clone_of")
    b.set_input("CLONE_OPTION", [1, target])
    return b


def make_delete_this_clone():
    """删除此克隆体"""
    return BlockBuilder("control_delete_this_clone")


def make_play_sound(sound_name):
    """播放声音"""
    b = BlockBuilder("sound_play")
    b.set_input("SOUND_MENU", [1, "sound_shadow"])
    return b


def make_playuntildone(sound_name):
    """播放声音直到结束"""
    b = BlockBuilder("sound_playuntildone")
    b.set_input("SOUND_MENU", [1, "sound_shadow"])
    return b


def make_stopallsounds():
    """停止所有声音"""
    return BlockBuilder("sound_stopallsounds")


def make_setvolumeto(volume):
    """音量设为 N%"""
    b = BlockBuilder("sound_setvolumeto")
    b.set_input("VOLUME", num(volume))
    return b


def make_changevolumeby(change):
    """音量增加 N"""
    b = BlockBuilder("sound_changevolumeby")
    b.set_input("VOLUME", num(change))
    return b


def make_setinstrument(inst_num):
    """将乐器设为 ..."""
    b = BlockBuilder("music_setInstrument")
    b.set_input("INSTRUMENT", [1, [4, str(inst_num)]])
    return b


def make_playdrum(beats):
    """击打 ... 拍"""
    b = BlockBuilder("music_playDrumForBeats")
    b.set_input("DRUM", [1, [4, "1"]])
    b.set_input("BEATS", num(beats))
    return b


def make_playnote(note, beats):
    """演奏音符 ... 拍"""
    b = BlockBuilder("music_playNoteForBeats")
    b.set_input("NOTE", [1, [7, str(note)]])
    b.set_input("BEATS", num(beats))
    return b


def make_rest(beats):
    """休止 ... 拍"""
    b = BlockBuilder("music_restForBeats")
    b.set_input("BEATS", num(beats))
    return b


def make_settempo(bpm):
    """将演奏速度设为 ..."""
    b = BlockBuilder("music_setTempo")
    b.set_input("TEMPO", num(bpm))
    return b


def make_ask(question):
    """询问 ... 并等待"""
    b = BlockBuilder("sensing_askandwait")
    b.set_input("QUESTION", string(question))
    return b


def make_resettimer():
    """计时器归零"""
    return BlockBuilder("sensing_resettimer")


def make_pen_clear():
    """清空画笔"""
    return BlockBuilder("pen_clear")


def make_pen_down():
    """落笔"""
    return BlockBuilder("pen_penDown")


def make_pen_up():
    """抬笔"""
    return BlockBuilder("pen_penUp")


def make_pen_stamp():
    """图章"""
    return BlockBuilder("pen_stamp")


def make_setpencolor(color_hex):
    """将画笔颜色设为 ..."""
    b = BlockBuilder("pen_setPenColorToColor")
    b.set_input("COLOR", [1, color_hex])
    return b


def make_setpensize(size):
    """将画笔大小设为 ..."""
    b = BlockBuilder("pen_setPenSizeTo")
    b.set_input("SIZE", num(size))
    return b


def make_changepensize(change):
    """将画笔大小增加 ..."""
    b = BlockBuilder("pen_changePenSizeBy")
    b.set_input("SIZE", num(change))
    return b


# Reporter 积木块（返回值）

def reporter_add():
    return BlockBuilder("operator_add")


def reporter_subtract():
    return BlockBuilder("operator_subtract")


def reporter_multiply():
    return BlockBuilder("operator_multiply")


def reporter_divide():
    return BlockBuilder("operator_divide")


def reporter_random():
    return BlockBuilder("operator_random")


def reporter_gt():
    return BlockBuilder("operator_gt")


def reporter_lt():
    return BlockBuilder("operator_lt")


def reporter_equals():
    return BlockBuilder("operator_equals")


def reporter_and():
    return BlockBuilder("operator_and")


def reporter_or():
    return BlockBuilder("operator_or")


def reporter_not():
    return BlockBuilder("operator_not")


def reporter_join():
    return BlockBuilder("operator_join")


def reporter_letter_of():
    return BlockBuilder("operator_letter_of")


def reporter_length():
    return BlockBuilder("operator_length")


def reporter_mod():
    return BlockBuilder("operator_mod")


def reporter_round():
    return BlockBuilder("operator_round")


def reporter_mathop():
    return BlockBuilder("operator_mathop")


def reporter_xposition():
    return BlockBuilder("motion_xposition")


def reporter_yposition():
    return BlockBuilder("motion_yposition")


def reporter_direction():
    return BlockBuilder("motion_direction")


def reporter_size():
    return BlockBuilder("looks_size")


def reporter_volume():
    return BlockBuilder("sound_volume")


def reporter_answer():
    return BlockBuilder("sensing_answer")


def reporter_mousedown():
    return BlockBuilder("sensing_mousedown")


def reporter_mousex():
    return BlockBuilder("sensing_mousex")


def reporter_mousey():
    return BlockBuilder("sensing_mousey")


def reporter_loudness():
    return BlockBuilder("sensing_loudness")


def reporter_timer():
    return BlockBuilder("sensing_timer")


def reporter_dayssince2000():
    return BlockBuilder("sensing_dayssince2000")


def reporter_username():
    return BlockBuilder("sensing_username")


def reporter_current():
    return BlockBuilder("sensing_current")


def reporter_music_tempo():
    return BlockBuilder("music_getTempo")


# null 常量（用于字段值）
null = None
