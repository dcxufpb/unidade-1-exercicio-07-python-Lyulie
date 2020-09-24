# coding: utf-8

def dados_loja_param(nome_loja, logradouro, numero, complemento, bairro,
                     municipio, estado, cep, telefone, observacao, cnpj,
                     inscricao_estadual):
    if not nome_loja:
        raise Exception ("O campo nome da loja é obrigatório")
    if not logradouro:
        raise Exception ("O campo logradouro do endereço é obrigatório")
    
    _logradouro = logradouro.strip() + ", "
    _numero = numero and str(numero) or "s/n"
    _complemento = complemento and " " + complemento or ""
    _bairro = bairro and bairro + " - " or ""

    if not municipio:
        raise Exception ("O campo município do endereço é obrigatório")
    _municipio = municipio + " - "

    if not estado:
        raise Exception ("O campo estado do endereço é obrigatório")
    
    _cep = cep and ("CEP:" + cep) or ""
    _telefone = telefone and ("Tel " + telefone) or ""
    _telefone = (_telefone and _cep) and (" " + _telefone) or _telefone
    _observacao = observacao and observacao or ""

    if not cnpj:
        raise Exception ("O campo CNPJ da loja é obrigatório")
    
    _cnpj = "CNPJ: " + cnpj

    if not inscricao_estadual:
        raise Exception ("O campo inscrição estadual da loja é obrigatório")
    
    _inscricao_estadual = "IE: " + inscricao_estadual
    
    return \
f"""{nome_loja}
{_logradouro}{_numero}{_complemento}
{_bairro}{_municipio}{estado}
{_cep}{_telefone}
{_observacao}
{_cnpj}
{_inscricao_estadual}"""
