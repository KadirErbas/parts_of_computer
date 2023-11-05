from django.db import models

# kategori
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
# ürün
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image_url = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

# anakart özellikleri
class MotherboardFeature(models.Model):
    processor_Socket_Type = models.CharField(max_length=255)
    ram_Type = models.CharField(max_length=255)
    compatible_Processors =models.CharField(max_length=255)
    motherboard_Size = models.CharField(max_length=255)
    
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product, self.processor_Socket_Type, self.ram_Type, self.compatible_Processors, self.motherboard_Size}"


# bilgisayar kasası özellikleri    
class ComputerCaseFeature(models.Model):
    case_Type = models.CharField(max_length=255)
    PSU = models.CharField(max_length=255)
    PSU_Location = models.CharField(max_length=255)
    transparent_Case = models.CharField(max_length=255)
    type_C = models.CharField(max_length=255)

    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product}, {self.case_Type}, {self.PSU}, {self.PSU_Location}, {self.transparent_Case}, {self.type_C}"


# ekrankartı özellikleri
class GraphicsCardFeature(models.Model):
    gpu_Manufacturer = models.CharField(max_length=255)
    gpu_Model = models.CharField(max_length=255)
    memory_Type = models.CharField(max_length=255)
    gpu_Memory_Capacity = models.CharField(max_length=255)

    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product}, {self.gpu_Manufacturer}, {self.gpu_Model}, {self.memory_Type}, {self.gpu_Memory_Capacity}"


# işlemci özellikleri
class ProcessorFeature(models.Model):
    processor_Model = models.CharField(max_length=255)
    processor_Manufacturer = models.CharField(max_length=255)
    processor_Socket_Type = models.CharField(max_length=255)
    processor_Series = models.CharField(max_length=255)
    core_Count = models.CharField(max_length=255)

    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product}, {self.processor_Model}, {self.processor_Manufacturer}, {self.processor_Socket_Type}, {self.processor_Series}, {self.core_Count}"


# kasa fanları özellikleri
class CaseFanFeature(models.Model):
    cooling_Type = models.CharField(max_length=255)
    fan_Count = models.CharField(max_length=255)
    led_Type = models.CharField(max_length=255)
    power_Connector = models.CharField(max_length=255)
    rpm = models.CharField(max_length=255)

    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product}, {self.cooling_Type}, {self.fan_Count}, {self.led_Type}, {self.power_Connector}, {self.rpm}"


# klavye özellikleri
class KeyboardFeature(models.Model):
    connection_Type = models.CharField(max_length=255)
    mechanical = models.BooleanField()
    keyboard_Layout = models.CharField(max_length=255)
    wrist_Support = models.BooleanField()
    numpad = models.BooleanField()

    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product}, {self.connection_Type}, {self.mechanical}, {self.keyboard_Layout}, {self.wrist_Support}, {self.numpad}"


# monitör özellikleri
class MonitorFeature(models.Model):
    screen_Size = models.CharField(max_length=255)
    resolution = models.CharField(max_length=255)
    refresh_Rate = models.CharField(max_length=255)
    panel_Type = models.CharField(max_length=255)
    response_Time = models.CharField(max_length=255)

    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product}, {self.screen_Size}, {self.resolution}, {self.refresh_Rate}, {self.panel_Type}, {self.response_Time}"


# fare özellikleri
class MouseFeature(models.Model):
    connection_Type = models.CharField(max_length=255)
    tracking_Type = models.CharField(max_length=255)
    button_Count = models.CharField(max_length=255)
    usage_Type = models.CharField(max_length=255)
    max_DPI = models.CharField(max_length=255)

    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product}, {self.connection_Type}, {self.tracking_Type}, {self.button_Count}, {self.usage_Type}, {self.max_DPI}"


# ram özellikleri
class RamFeature(models.Model):
    ram_Type = models.CharField(max_length=255)
    ram_Capacity = models.CharField(max_length=255)
    ram_Frequency = models.CharField(max_length=255)
    channel_Type = models.CharField(max_length=255)
    ram_Compatibility = models.CharField(max_length=255)

    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product}, {self.ram_Type}, {self.ram_Capacity}, {self.ram_Frequency}, {self.channel_Type}, {self.ram_Compatibility}"


# soğutucular özellikleri
class CoolerFeature(models.Model):
    compatible_Sockets = models.CharField(max_length=255)
    led = models.CharField(max_length=255)
    radiator_Size = models.CharField(max_length=255)
    fan_Count = models.IntegerField()

    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product}, {self.compatible_Sockets}, {self.led}, {self.radiator_Size}, {self.fan_Count}"
