import pickle
import cellphone

FILENAME = 'cellphones.dat'
def main():
    end_of_file = False
    input_file=open(FILENAME,'rb')
    while not end_of_file:
        try:
            phone=pickle.load(input_file)
            display_data(phone)
        except EOFError:
            end_of_file=True
    input_file.close()
def display_data(phone):
    print("manufacturer:",phone.get_manufact())
    print("model number:",phone.get_model())
    print("retail price :$",format(phone.get_retail_price(),",.2f"),sep='')
main()