class BasicPlan:
    can_stream = True
    can_download = True
    num_of_devices = 1
    has_SD = True
    has_HD = False
    has_UHD = False
    price = '$8.99'
    
class StandardPlan(BasicPlan):
    num_of_devices = 2
    has_HD = True
    price = '$12.99'


class PremiumPlan(StandardPlan):
    num_of_devices = 4
    has_UHD = True
    price = '$15.99'