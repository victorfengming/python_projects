# 需求:
	# 可依次选择进入各子菜单
	# 可从任意一层往回退到上一层
	# 可从任意一层退出程序

menu = {
	'北京':{
		'海淀':{...},
		'昌平':{
			'沙河':{
				'老男孩':{...},
				'贼溜啊':{...},	
			},
			'天通苑':{
			'这样':{
			'那样的':{...},
			'啥样的':{
				'王':{
					'李':{...},
				}
			},
			
			},
			},
			'回龙观':{
			
			},
		},
		'朝阳':{...},
		'东城':{...},
	},
	'上海':{
		'闽行':{...},
		'闸北':{...},
		'浦东':{...},
	},
	'山东':{
		'济南':{
			
			'景点':{},
			'美食':{},
			'商场':{},
			'银行':{},
			'医院':{},
			'电影院':{},
			'KTV':{},
			'酒店':{},
			'加油站':{},
		},
		'青岛':{
		
			'景点':{},
			'美食':{},
			'商场':{},
			'银行':{},
			'医院':{},
			'电影院':{},
			'KTV':{},
			'酒店':{},
			'加油站':{},
		},
		'淄博':{...},
		'枣庄':{...},
		'东营':{...},
		'烟台':{
		
			'景点':{},
			'美食':{},
			'商场':{},
			'银行':{},
			'医院':{},
			'电影院':{},
			'KTV':{},
			'酒店':{},
			'加油站':{},
		},
		'潍坊':{...},
		'济宁':{...},
		'潍坊':{...},
		'泰安':{...},
		'威海':{...},
		'日照':{...},
		'莱芜':{...},
	},
}
	
while True:		#进入第一层
	for k in menu:
		print(k)
	choice = input(">>:").strip()
	if not choice: continue
	if choice in menu:
		while True:		#进入第二层
			for k in menu[choice]:
				print(k)
			choice2 = input(">>:").strip()
			if not choice: continue
			if choice2 in menu[choice]:
				while True:			 #进入第三层
					#print('go to',menu[choice][choice2])
					for k in menu[choice][choice2]:
						print(k)
					choice3 = input(">>>:").strip()
					if not choice3 : continue
					if choice3 in menu[choice][choice2]:
						print("go to ",menu[choice][choice2][choice3])
					elif choice3 == 'b':
						break
					else:
						print("节点不存在,请重新输入")
			elif choice2 == 'b':
				break
						
			else:
				print("节点不存在,请重新输入")
	else:
		print("节点不存在,请重新输入")
# 虽然我只是代码新手,但是我感觉我重复写了很多代码.
# 现在我只是实现功能,没有想到如何优化代码
# 这就是 苦逼的 普通青年版代码
# 功能还有限欠缺
# 但是不想实现了,太tm费劲了
# 由于上次课的功能还没有完善全面,所以呢,这节课在添加功能
