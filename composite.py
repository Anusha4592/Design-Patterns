class Equipment(object):

    def Power(self):
        pass

    def NetPrice(self):
        pass

    def DiscountPrice(self):
        pass

    def Add(self, equip):
        pass

    def Remove(self, equip):
        pass

    def CreateIterator(self):
        pass


class FloppyDisk(Equipment):

    def Power(self):
        return 10 

    def NetPrice(self):
        return 13

    def DiscountPrice(self):
        return 1

class Card(Equipment):

    def Power(self):
        return 5 

    def NetPrice(self):
        return 8

    def DiscountPrice(self):
        return 1


class CompositeEquipment(Equipment):

    def __init__(self):
        self._equipment = []
    
    def Power(self):
        equipments = self.CreateIterator()
        power_total = 0
        for equip in equipments:
            power_total += equip.Power()
        return power_total
       

    def NetPrice(self):
        import pdb;pdb.set_trace()
        equipments = self.CreateIterator()
        netprice_total = 0
        for equip in equipments:
            netprice_total += equip.NetPrice()
        return netprice_total

    def DiscountPrice(self):
        equipments = self.CreateIterator()
        discount_total = 0
        for equip in equipments:
            discount_total += equip.NetPrice()
        return discount_total

    def Add(self, equip):
        self._equipment.append(equip)
        return "Adds to Equipment"

    def Remove(self, equip):
        self._equipment.remove(equip)
        return "Removes from Equipment"

    def CreateIterator(self):
        return iter(self._equipment)



class Chassis(CompositeEquipment):
    pass
    #def Power(self):
    #    return 15

    #def NetPrice(self):
    #    return 12

    #def DiscountPrice(self):
    #    return 1

class Bus(CompositeEquipment):
    pass
    #def Power(self):
    #    return 3

    #def NetPrice(self):
    #    return 2

    #def DiscountPrice(self):
    #    return 1


if __name__ == '__main__':
    chassis = Chassis()

    floppy = FloppyDisk()
    card = Card()

    bus = Bus()
    bus.Add(card)

    chassis.Add(floppy)
    chassis.Add(bus)
    net_price = chassis.NetPrice()
    print net_price

