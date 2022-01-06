import json
from  conversion import util
import re

class Currency:

    def __init__(self, currency_type):
        self.currency_type = currency_type
        self.currency_config = util.read_mapping_file()[currency_type]
        # import pdb;pdb.set_trace()
        self.denomination = self.currency_config["denomination"]
        self.minimum_currency = self.currency_config["minimum_currency"]
        self.convertor_dict = self.currency_config["convertor"]

    def create_denomination_dict(self):
        new_denom_dict={}
        for i in self.denomination:
            dig=float(re.findall(r'\d+(?:[.]\d+)*',i)[0])
            curr=re.sub(r'\d+(?:[.]\d+)*', "", i)
            if curr in self.convertor_dict:
                dig*= self.convertor_dict[curr]
                new_denom_dict[dig] = {"orig_val":i}
            else:
                print(curr)
                raise ValueError("digit not present in config file ")
        new_denom_dict = self.rearrange_denominations(new_denom_dict)
        return new_denom_dict

    def rearrange_denominations(self, new_denom_dict):
        tmp_denominations={}
        for key in reversed(sorted(new_denom_dict)):
            tmp_denominations[key] = new_denom_dict[key]
        return tmp_denominations

    def max_conversion_value(self):
        all_values = self.convertor_dict.values()
        max_value = max(all_values)
        return max_value
    
    def max_conversion_key(self):
        max_key = max(self.convertor_dict, key=self.convertor_dict.get)
        return max_key

    def convert_original_values_to_float(self, input):
        max_val = self.max_conversion_value()
        amount_int = float(re.findall(r'\d+(?:[.]\d+)*',input)[0])
        amount_curr = re.sub(r'\d+(?:[.]\d+)*', "", input)
        if amount_curr in self.convertor_dict:
            converted_val = amount_int*self.convertor_dict[amount_curr]/max_val
        else:
            raise ValueError("Please enter valid symbol in input values")
        return converted_val

        



    def convert_values(self, input_amount):
        nominals = self.create_denomination_dict()
        input_amount*=self.max_conversion_value()
        output = {}
        
        for n in nominals:
            output[n] = input_amount // n
            input_amount %= n
        for k, v in output.items():
            if v>0:
                print(f'{nominals[k]["orig_val"]} * {int(v)}')
    def preprocess_money(self, input_money):
        input_amount*=self.max_conversion_value()


    def get_money_after_purchase(self, amount, product_price):
        converted_amount = self.convert_original_values_to_float(amount)
        converted_product_price = self.convert_original_values_to_float(product_price)
        deducted_money = converted_amount-converted_product_price
        if deducted_money<0:
            print("please enter amount bigger than product price")
            return
        self.convert_values(deducted_money)
        print(f'Total change: {self.max_conversion_key()}{deducted_money}')
        return f'Total change: {self.max_conversion_key()}{deducted_money}'



        


    

    




