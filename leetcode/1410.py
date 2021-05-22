def entityParser(text:str):
    '''
    双引号：字符实体为 &quot; ，对应的字符是 " 。
    单引号：字符实体为 &apos; ，对应的字符是 ' 。
    与符号：字符实体为 &amp; ，对应对的字符是 & 。
    大于号：字符实体为 &gt; ，对应的字符是 > 。
    小于号：字符实体为 &lt; ，对应的字符是 < 。
    斜线号：字符实体为 &frasl; ，对应的字符是 / 。
    :param text:
    :return:
    '''
    text = text.replace("&quot;",'"')
    """
    同
    """
    return text

print(entityParser("and I quote: &quot;...&quot;"))