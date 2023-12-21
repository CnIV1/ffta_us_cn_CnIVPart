#! python3
# coding: utf-8

ocr_ambiguous_s = {
    0x409: '紧',
    0x455: '啵',
    0xb27: '务',
    0x3db: '竞',
    0x311: '竟',
    0x628: '终',
    0x5a9: '志',
    0x4fd: '忐',
    0x343: '忑',
    0x7f3: '态',
    0x9c6: '肇',
    0x71a: '咦',
    0x878: '羡',
    0x17b: '样',
    0xade: '哦',
    0x32c: '蜴',
    0xab4: '报',
    0x907: '盗',
    0xb39: '盔',
    0x49f: '乎',
    0x4d0: '效',
    0x3cb: '拒',
    0x1d2: '速',
    0x180: '赖',
    0x8b9: '颗',
    0x7bd: '搜',
    0x380: '弃',
    0x63f: '叔',
    0x734: '馈',
    0x9d8: '寞',
    0x16c: '案',
    0x3a2: '喊',
    0xb7a: '雄',
    0xbdf: '领',
    0x479: '嫌',
    0x23a: '隐',
    0xafc: '魔',
    0x302: '确',
    0x893: '痛',
    0x578: '索',
    0x2b0: '河',
    0x1e9: '阿',
    0x7e0: '多',
    0xa2a: '缪',
    0x9cd: '滚',
    0x86c: '宠',
    0x42d: '窟',
    0x603: '释',
    0x475: '剑',
    0x970: '醺',
    0xc0a: '联',
    0x3c7: '给',
    0x9c7: '找',
    0x8ff: '麝',
    0xc33: '嘛',
    0xb23: '脉',
    0xa6b: '服',
    0x4c2: '擒',
    0xafb: '磨',
    0x8af: '庭',
    0x704: '睡',
    0x535: '彻',
    0x501: '衡',
    0xc26: '啫',
    0x15a: '味',
    0x6c0: '嗦',
    0xaa6: '亏',
    0x3a1: '议',
    0x594: '算',
    0x8f4: '倒',
    0x9d7: '搞',
    0x731: '精',
    0xc0c: '炼',
    0x428: '咯',
    0x9e8: '繁',
    0x7d4: '续',
    0x9aa: '卖',
    0x7c4: '蔑',
    0x7ed: '体',
    0x17e: '驹',
    0x16f: '教',
    0x711: '数',
    0x55f: '栽',
    0x932: '匿',
    0x189: '移',
    0xaa8: '穆',
    0x1fe: '糟',
    0x858: '着',
    0x67a: '汝',
    0x1d3: '待',
    0x943: '蹭',
    0x786: '曾',
    0x2b5: '豫',
    0x9cb: '玫',
    0xaac: '呜',
    0x3ed: '盯',
    0x6d3: '侵',
    0x57c: '哟',
    0x432: '惧',
    0x21a: '畏',
    0x42f: '眩',
    0x3f8: '晓',
    0x256: '婴',
    0xb05: '幕',
    0x942: '妒',
    0x4ad: '糊',
    0x255: '营',
    0x7ec: '锏',
    0x787: '肆',
    0xab9: '崩',
    0x55b: '霆',
    0x3ee: '胸',
    0x52f: '昏',
    0x59a: '餐',
    0x9c0: '缚',
    0x6cc: '触',
    0x35d: '陷',
    0x921: '腾',
    0x4b9: '互',
    0x81c: '脱',
    0x911: '答',
    0x56c: '莉',
    0xc36: '腕',
    0x7b7: '歹',
    0xb3a: '摸',
    0x16e: '率',
    0x77a: '蜥',
    0x766: '洗',
    0x816: '绕',
    0x6cd: '食',
    0x212: '威',
    0x4b6: '顾',
    0x77b: '闪',
    0x375: '寄',
    0x93c: '蝠',
    0x3ac: '丢',
    0x9d4: '黛',
    0x5cf: '磁',
    0x5cb: '滋',
    0x229: '溢',
    0x9bc: '薄',
    0x56e: '咬',
    0x31a: '滑',
    0xa16: '猾',
    0xb22: '唉',
    0xa76: '喷',
    0x940: '圆',
    #'①②③④⑤⑥⑦⑧⑨⑩'
    0x38e: '③',
    0x3ae: '客',
    0xa8a: '并',
    0x80e: '泽',
    0x49b: '绎',
    0x867: '著',
    0xc06: '拂',
    0x196: '察',
    0x55a: '祭',
    0xac7: '蓬',
    0x6a5: '篷',
    0xb4f: '稳',
    0xa9a: '返',
    0x941: '删',
    0xb89: '搖', # 也是摇，字库里多了一个，可能跟改字版有关，总之用异体字表示
    0x3d2: '摇',
    0x477: '圈',
    0x31d: '②',
    0x790: '素',
    0xaf6: '奔',
    0x459: '髻',
    0xb81: '簪',
    0x1da: '编',
    0x7f4: '戴',
    0x5b1: '狮',
    0xc3c: '蘑',
    0xc2d: '锻',
    0x154: '言',
    0xc50: '箍',
    0xac1: '烹',
    0x265: '疫',
    0x529: '困',
    0x8e9: '渡',
    0x9a3: '培',
    0xbe9: '麟',
    0xac8: '蜂',
    0x5c8: '慈',
    0x803: '蝎',
    0x959: '缀',
    0x7ad: '燥',
    0x5e5: '湿',
    0x2bd: '霸',
    0x98c: '覇', # 重复字，异体字表示
}

ocr_ambiguous = {
    # conflict
    0x31d: '②',
    0x38e: '③',
    0x17b: '样',
    0x32c: '蜴',
    0x791: '组',
    0x7d2: '贼',
    0xb68: '优',
    0xb6e: '忧',
    0x752: '窃',
    0x5a9: '志',
    0x343: '忑',
    0x940: '圆',
    0x80e: '泽',
    0x49b: '绎',
    0xac7: '蓬',
    0x6a5: '篷',
    0x315: '喝',
    0x4ca: '交',
    0x15e: '变',
    0x4f7: '诅',
    0x941: '删',
    0x57e: '册',
    0x234: '怡',
    0x316: '恰',
    0x2bd: '霸',
    0x98c: '覇', # 异体字
    0x6a0: '兹',
    0x57c: '哟',
    0x1ad: '踏',
    0x943: '蹭',
    # nondet
    0x7ec: '锏',
    0x959: '缀',
    0x9ce: '盏',
    0xc2d: '煅',
    0x705: '瞑',
    0xb89: '摇',
    0x3d2: '搖', # 异体字
    0x718: '颇',
    0xb3a: '摸',
    0x455: '啵',
}
