class log:
    log_path = "../file/log.json"
    def __init__(self) -> None:
        pass

    @staticmethod
    def read_log():
        """
        读日志接口
        在ui.py(&?)中调用
        ui.py中的需求是返回指定内容的一段日志 如指定用户、指定时间段
        Parameters: 
            TODO
        Returns:
            TODO
        Raises:
            TODO
        """
        pass
    
    @staticmethod
    def write_log():
        """
        写日志接口
        在monitor.py和setting.py中调用
        Parameters: 
            TODO
        Returns:
            TODO
        Raises:
            TODO
        """
        pass