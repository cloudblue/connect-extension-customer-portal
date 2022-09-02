def normalized_object(obj, key_prefix='', obj_data=None):
    if obj_data is None:
        obj_data = []
        
    for key, value in obj.items():
        property_value = None
        if isinstance(value, dict):
            normalized_object(
                value,
                f"{key_prefix}{'.' if key_prefix else ''}{key}",
                obj_data,
            )
        elif isinstance(value, list) or isinstance(value, set):
            if isinstance(value[0], str):
                property_value = ', '.join(value)
            elif isinstance(value[0], dict):
                for index, v in enumerate(value):
                    normalized_object(
                        v,
                        f"{key_prefix}{'.' if key_prefix else ''}{key}[{index}]",
                        obj_data,
                    )
        else:
            property_value = value
        
        if property_value:
            obj_data.append({
              'property': f"{key_prefix}{'.' if key_prefix else ''}{key}",
              'value' : property_value,
            })
    
    return obj_data
