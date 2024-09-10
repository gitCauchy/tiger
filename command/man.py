from conf import function_info_read


def man(func_name):
    func_dict = function_info_read.read_function_config(func_name)
    module_name = func_dict["module_name"]
    file_name = func_dict["file_name"]
    class_name = func_dict["class_name"]
    module = __import__("core")
    sub_module = getattr(module, module_name)
    m_py = getattr(sub_module, file_name)
    _class = getattr(m_py, class_name)
    obj = _class()
    getattr(obj, 'man')()
