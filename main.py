def make_dict():
  datas = []
  i_branching = input_data['values']['categories']['1225']['branching']
  i_custom_fields = input_data['values']['categories']['1225']['custom_fields']

  for i in i_custom_fields:
    data = {}
    data['field_label'] = i['label']
    data['field_options'] = [j['label'] for j in i['options']]
    data['field_type'] = i['type']
    data['field_name'] = i['name']
    data['field_rules_status'] = i['rules_status']
    data['field_conditional'] = i['is_conditional']
    data['field_rules'] = i['rules']
    data['field_required'] = i['required']
    datas.append(data)

  for i in i_branching:
    data = {}
    data['subfield_label'] = i['label']
    data['subfield_options'] = [j['label'] for j in i['options']]
    data['subfield_type'] = i['type']
    data['subfield_name'] = i['name']
    data['subfield_rules_status'] = i['rules_status']
    data['subfield_rules'] = i['rules']
    data['subfield_required'] = i['required']
    data['subfield_conditional'] = i['is_conditional']
    datas.append(data)
  

  
  redata