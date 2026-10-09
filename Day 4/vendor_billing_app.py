
'''This is Vendor-Product billing app'''
import time

class Vendor:
    '''This is vendor class - initialize vendor details'''

    def __init__(self, vName, vGST):
        '''Initialize vendor details'''
        self.vName = vName
        self.vGST = vGST
        print(f'Vendor {self.vName} enrollment is done')

    def billing(self, pName, pQty=0, pCost=0.0):
        '''Perform product billing and update log file'''
        self.pName = pName
        self.pQty = pQty
        self.pCost = pCost

        self.total = self.pCost * self.pQty
        self.tax = self.total * 0.18
        self.gs = self.total + self.tax

        s1 = f'{self.vName}\t{self.vGST}\t{self.pName}\t{self.pQty}'
        s2 = f'\t{self.pCost}\t{self.total}\t{self.gs}'
        s3 = f'\t{time.ctime()}\n\n'

        with open('vendor_prods.log', 'a') as wobj:
            wobj.write(s1 + s2 + s3)

        print(f'Product: {self.pName}')
        print(f'Total: {self.total}')
        print(f'GST: {self.tax}')
        print(f'Grand Total: {self.gs}')
        print('Billing saved to vendor_prods.log\n')


# Create vendor objects
vobj1 = Vendor('Klabs', 'GST1234')
vobj2 = Vendor('Xserver', 'GST5593')

# Perform billing
vobj1.billing('pA', 5, 1250)
vobj2.billing('pB', 2, 435.2)

# Display documentation
print('Class documentation:', Vendor.__doc__)
print('Billing documentation:', Vendor.billing.__doc__)