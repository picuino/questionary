import os
for filename in os.listdir('.'):
    if filename[-4:].lower() in ['.png', '.jpg']:
        print('![](images/thumbs/%s)' % filename)
input('Pulsa Enter')
