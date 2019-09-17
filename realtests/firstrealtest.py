def main():
    cars = {'number':3,
            'vehicles': [{'brand': 'Kia', 'model':'Soul'},{'brand':'Tesla', 'model':'ModelS'},{'brand':'Chevy','model':'Tahoe'}],
            'colors':['red','white','blue']}
    print(f"I have {cars['number']} cars, a {cars['colors'][0]} {cars['vehicles'][0]['brand']} {cars['vehicles'][0]['model']}, a {cars['colors'][1]} {cars['vehicles'][1]['brand']} {cars['vehicles'][1]['model']}, a {cars['colors'][2]} {cars['vehicles'][2]['brand']} {cars['vehicles'][2]['model']}." )
main()
