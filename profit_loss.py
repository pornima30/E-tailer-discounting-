""" Profit and Loss """
#  pylint:disable=invalid-name


def decide_discount(list_price, cost_price):
    """ Decides discount """
    quantity = int(input("Enter the quantity of product sold per month: "))
    if quantity > 500:
        return 0, 100
    if quantity > 200:
        return 15, (list_price*(0.85) - cost_price)*100/cost_price
    retain_product = str(input(
        "Did the average sales of the current product exceeds 200 per month(Y/N)?: ")).lower()
    if retain_product == 'n':
        return {"errorMsg": "Product is no longer profitable and Removed!"}
    return 35, (list_price*(0.65) - cost_price)*100/cost_price


def price_setting():
    """ Sets prices """
    purchasing_price = float(input("enter purchasing price: "))
    new_supplier = str(input("First time user(Y/N)?: ")).lower()
    if new_supplier not in ['n', 'y']:
        return True, {"errorMsg": f"{new_supplier} not a valid response"}, None
    if new_supplier == 'y':
        days_since_reg = int(input("Enter the days since you registered?: "))
        if days_since_reg < 60:
            list_price = purchasing_price*2
            discount_percent = 0
            profit_percent = ((list_price - purchasing_price)
                              * 100)/purchasing_price
            return False, discount_percent, profit_percent
        product_reg_days = int(
            input("Enter the days you had registered this product?: "))
        if product_reg_days < 0:
            return True, {
                "errorMsg": f"{product_reg_days} is not an acceptable value"
            }, None
        if product_reg_days > 30:
            list_price = purchasing_price*2
            discount_percent, profit_percent = decide_discount(
        purchasing_price*2, purchasing_price)
            return False, discount_percent, profit_percent
        list_price = purchasing_price*2
        discount_percent = 0
        profit_percent = (list_price - purchasing_price)*100/purchasing_price
        return False, discount_percent, profit_percent
    discount_percent, profit_percent = decide_discount(
        purchasing_price*2, purchasing_price)
    return False, discount_percent, profit_percent


error, discount, profit = price_setting()
error_msg = discount
if error:
    print(error_msg)
else:
    print(f"Discount %: {discount}")
    print(f"Profit %: {profit}")
