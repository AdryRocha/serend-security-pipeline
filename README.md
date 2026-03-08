# 🛡️ serend-security-pipeline

Laboratório de segurança — pipeline com análise SAST e secret scanning

## ⚠️ AVISO IMPORTANTE

Este repositório contém código **intencionalmente vulnerável** 
criado exclusivamente para fins educacionais e testes de SAST.

**Nunca comite credenciais reais em repositórios, 
mesmo privados.**

## 🎯 Objetivo

Simular um pipeline de segurança com:
- Análise estática de código (SAST) com CodeQL
- Detecção de segredos com TruffleHog  
- Verificação de dependências vulneráveis com Safety

## 🧪 Vulnerabilidades propositais incluídas

| Arquivo | Vulnerabilidade | OWASP |
|---------|----------------|-------|
| app.py | SQL Injection | A03 |
| app.py | Credenciais hardcoded | A07 |
| app.py | Hash MD5 fraco | A02 |
| requirements.txt | Dependências desatualizadas | A06 |

## 👩‍💻 Autora

Adriana Rocha — Laboratório prático de Cibersegurança
```

