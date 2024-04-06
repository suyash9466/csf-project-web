import hashlib as csf
from pyscript import document


def sha3_224_converter(event):      
    pwd = document.getElementById('sha3_224_input').value
    it = csf.sha3_224(pwd.encode('utf-8'))
    ai = it.hexdigest()
    print(ai)
    output_div = document.getElementById('sha3_224_output')
    output_div.innerText = ai