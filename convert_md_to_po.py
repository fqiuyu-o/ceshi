#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将 Markdown 格式的药品注册管理办法转换为 PO 翻译文件
Convert Drug Registration Management Measures from Markdown to PO format
"""

import re
from datetime import datetime

def parse_markdown_to_po(md_file, pot_file, po_file_en):
    """解析 Markdown 文件并生成 POT 和 PO 文件"""
    
    # 读取 Markdown 文件
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # POT 文件头部
    pot_header = f"""# Translation template for Drug Registration Management Measures
# 药品注册管理办法翻译模板
# Copyright (C) {datetime.now().year}
#
msgid ""
msgstr ""
"Project-Id-Version: Drug Registration Management Measures 1.0\\n"
"Report-Msgid-Bugs-To: \\n"
"POT-Creation-Date: {datetime.now().strftime('%Y-%m-%d %H:%M+0000')}\\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\\n"
"Language-Team: LANGUAGE <LL@li.org>\\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"

"""
    
    # PO 文件头部（英文）
    po_header = f"""# English translation for Drug Registration Management Measures
# 药品注册管理办法英文翻译
# Copyright (C) {datetime.now().year}
#
msgid ""
msgstr ""
"Project-Id-Version: Drug Registration Management Measures 1.0\\n"
"Report-Msgid-Bugs-To: \\n"
"POT-Creation-Date: {datetime.now().strftime('%Y-%m-%d %H:%M+0000')}\\n"
"PO-Revision-Date: {datetime.now().strftime('%Y-%m-%d %H:%M+0000')}\\n"
"Last-Translator: Translation Team <team@example.com>\\n"
"Language-Team: English\\n"
"Language: en\\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"
"Plural-Forms: nplurals=2; plural=(n != 1);\\n"

"""
    
    pot_entries = []
    po_entries = []
    
    # 按行分割内容
    lines = content.strip().split('\n')
    
    chapter_count = 0
    article_count = 0
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # 匹配章节标题（如：第一章  总  则）
        if re.match(r'^第[一二三四五六七八九十百]+章', line):
            chapter_count += 1
            context = f"chapter{chapter_count}"
            pot_entries.append(f'#: {context}\nmsgid "{line}"\nmsgstr ""\n')
            po_entries.append(f'#: {context}\nmsgid "{line}"\nmsgstr ""\n')
        
        # 匹配条款（如：第一条  ...）
        elif re.match(r'^第[一二三四五六七八九十百]+条', line):
            article_count += 1
            context = f"article{article_count}"
            # 转义引号
            escaped_line = line.replace('"', '\\"')
            pot_entries.append(f'#: {context}\nmsgid "{escaped_line}"\nmsgstr ""\n')
            po_entries.append(f'#: {context}\nmsgid "{escaped_line}"\nmsgstr ""\n')
        
        # 其他段落
        else:
            context = f"para{len(pot_entries) + 1}"
            escaped_line = line.replace('"', '\\"')
            pot_entries.append(f'#: {context}\nmsgid "{escaped_line}"\nmsgstr ""\n')
            po_entries.append(f'#: {context}\nmsgid "{escaped_line}"\nmsgstr ""\n')
    
    # 写入 POT 文件
    with open(pot_file, 'w', encoding='utf-8') as f:
        f.write(pot_header)
        f.write('\n'.join(pot_entries))
    
    # 写入 PO 文件（英文）
    with open(po_file_en, 'w', encoding='utf-8') as f:
        f.write(po_header)
        f.write('\n'.join(po_entries))
    
    print(f"✅ 成功生成翻译文件！")
    print(f"   - POT 模板: {pot_file}")
    print(f"   - PO 英文: {po_file_en}")
    print(f"   - 共提取 {len(pot_entries)} 个翻译条目")

if __name__ == "__main__":
    md_file = "药品注册管理办法.md"
    pot_file = "drug_registration.pot"
    po_file_en = "drug_registration_en.po"
    
    parse_markdown_to_po(md_file, pot_file, po_file_en)
