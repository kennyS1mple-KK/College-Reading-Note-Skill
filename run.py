# 大学生读书笔记与复习助手 - 模拟引擎
# 这是一个简单的逻辑处理程序，用来模拟 SKILL.md 的处理流程

def note_assistant(input_text):
    # 1. 边界条件：字数检查
    if len(input_text) < 50:
        return "同学，这段文字太短啦，请提供更完整的段落才能生成有效的笔记哦。"

    # 2. 提取核心观点 (模拟处理)
    output = "【核心观点】\n"
    output += "（此处应由AI概括）：" + input_text[:30] + "...\n\n"

    # 3. 分支逻辑：名词解释
    # 这里通过简单判断是否存在“经济”、“历史”等词来演示分支逻辑
    output += "【概念解析】\n"
    if "经济" in input_text or "价值" in input_text:
        output += "- 名词解释：已识别到经济学概念，正在进行通俗化处理。\n\n"
    else:
        output += "- 本文通俗易懂，未发现深奥专有名词。\n\n"

    # 4. 分支逻辑：历史类文本考题生成
    output += "【复习自测】\n"
    if "1929" in input_text or "年代" in input_text:
        output += "1. 文中提到的关键历史时间节点是？\n"
        output += "2. 针对该事件的评价是否具有历史局限性？\n"
    else:
        output += "1. 根据文中内容，你如何理解核心论点？\n"
        output += "2. 请举例说明该概念在现实生活中的应用。\n"
    
    return output

# --- 测试运行 ---
if __name__ == "__main__":
    # 测试用例 1：短文本 (触发边界)
    print("测试1：", note_assistant("今天天气很好。"))
    
    # 测试用例 2：经济类文本 (触发经济学逻辑)
    print("\n测试2：", note_assistant("机会成本是指为了得到某种东西而放弃另一样东西的最大价值。选择是稀缺的。"))