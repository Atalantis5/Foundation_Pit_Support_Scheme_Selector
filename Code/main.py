#输入模块（后期转换成可视化按钮选择）
##步骤一：输入
def get_input():
    foundation_pit_assignment = input('请输入基坑参数【深度(m)/底面积(m^2)/形状】:').split()
    geological_conditions = input('请输入地质条件【土层类型/地下水位(m)/承载力(kPa)】:').split()
    environmental_assignment = input('请输入环境参数【周边建筑/管线分布/交通流量】:').split()
    construction_requirements = input('请输入【工期(天)/设备限制/成本预算（万）】:').split()
    model = {
        'FoundationPitAssignment':{
            'depth':0.0,
            'size':0.0,
            'shape':'未知'
        },
        'GeologicalConditions':{
            'earth_type':'未知',
            'underground_water_level':0.0,
            'bearing_capacity':0.0
        },
        'EnvironmentalAssignment':{
            'surrounding_buildings':'未知',
            'piping_distribution':'未知',
            'traffic_flow':'未知'
        },
        'ConstructionRequirements':{
            'deadline':0,
            'equipment_limit':'未知',
            'cost_budget':0.0
        }
    }
    try:
        if len(foundation_pit_assignment) and len(geological_conditions) and len(environmental_assignment) and len(construction_requirements)!=3:
            raise ValueError('需要输入三个参数')
        model['FoundationPitAssignment']['depth'] = float(foundation_pit_assignment[0])
        model['FoundationPitAssignment']['size']  = float(foundation_pit_assignment[1])
        model['FoundationPitAssignment']['shape']= foundation_pit_assignment[3]
        if model['FoundationPitAssignment']['shape'].isalpha():
            raise ValueError('需要输入字符串')

        model['GeologicalConditions']['earth_type'] = geological_conditions[0]
        if model['GeologicalConditions']['earth_type'].isalpha():
            raise ValueError('需要输入字符串')
        model['GeologicalConditions']['underground_water_level'] = float(geological_conditions[1])
        model['GeologicalConditions']['bearing_capacity'] = float(geological_conditions[2])

        model['EnvironmentalAssignment']['surrounding_buildings'] = environmental_assignment[0]
        model['EnvironmentalAssignment']['piping_distribution'] = environmental_assignment[1]
        model['EnvironmentalAssignment']['surrounding_buildings'] = environmental_assignment[2]
        if model['EnvironmentalAssignment']['surrounding_buildings'].isalpha() or model['EnvironmentalAssignment']['piping_distribution'].isalpha() or model['EnvironmentalAssignment']['surrounding_buildings'].isalpha():
            raise ValueError('需要输入字符串')

        model['ConstructionRequirements']['deadline'] = int(construction_requirements[0])
        model['ConstructionRequirements']['equipment_limit'] = construction_requirements[1]
        if model['ConstructionRequirements']['equipment_limit'].isalpha():
            raise ValueError('需要输入字符串')
        model['ConstructionRequirements']['cost_budget'] = float(construction_requirements[2])

        return model
    except ValueError as e:
            print(f"输入错误: {e}\n请重新输入:")
    except Exception as e:
            print(f"未知错误: {e}\n请重新输入:")

model1 = get_input()
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
