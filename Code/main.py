#输入模块（后期转换成可视化按钮选择）
##步骤一：输入
def get_input():
    depth,size,form = get_valid_input('foundation_pit_assignment','请输入基坑参数【深度(m)/尺寸/形状】:')
    layer_type,underground_water_level,bearing_capacity= get_valid_input('geological_conditions','请输入地质条件【图层类型/地下水位/承载力】:')
    surrounding_buildings,pipeline_distribution,traffic_flow= get_valid_input('environmental_assignment','请输入环境参数【周边建筑/管线分布/交通流量】:')
    time_limit,equipment_constraints,cost_budget= get_valid_input('construction_requirements','请输入【工期/设备限制/成本预算】:')

##步骤二：错误输入处理
def get_valid_input(date_type,welcome_word='请输入'):
    while True:
        try:
            # 获取并分割输入（假设输入格式：num1 num2 string）
            inputs = input(welcome_word).split()

            if len(inputs) != 3:
                raise ValueError("需要输入三个参数")

            # 验证数字部分
            match date_type:
                case 'foundation_pit_assignment':
                    num1 = float(inputs[0])
                    num2 = float(inputs[1])
                    if not inputs[2].isalpha():
                        raise ValueError("字符串必须只包含字母")
                    return num1,num2,inputs[2]
                case 'geological_conditions':
                    if not inputs[0].isalpha():
                        raise ValueError("字符串必须只包含字母")
                    num1 = float(inputs[1])
                    num2 = float(inputs[2])
                    return inputs[0],num1,num2
                case 'environmental_assignment':
                    return inputs[0],inputs[1],inputs[2]
                case 'construction_requirements':
                    num1 = float(inputs[0])
                    if not inputs[1].isalpha():
                        raise ValueError("字符串必须只包含字母")
                    num2 = inputs[2]
                    return num1,inputs[1],num2

        except ValueError as e:
            print(f"输入错误: {e}\n请重新输入:")
        except Exception as e:
            print(f"未知错误: {e}\n请重新输入:")
##步骤三：数据格式化

##步骤四：生成工程模型（数据格式：字典+列表+元组）

#方案匹配引擎

##多层嵌套决策树

##敏感环境预警

##危险环境报错

#循环验证系统

##稳定性校核

##经济性复核

##可行性检查

#结果输出界面

##三位支护可视化

##施工顺序（动画演示）

##材料清单（自动生成）

##风险预警报告（PDF/Excel）

##针对性用户界面
