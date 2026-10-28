# Segurança e privacidade

**Laboratório educacional:** utilizar apenas dados sintéticos, nunca coordenadas reais de pessoas ou clientes.

Antes de qualquer uso produtivo, implementar:
- Identificação, autenticação e rotação de credenciais por dispositivo.
- Autorização por tenant e por veículo em escrita e leitura.
- Proteção contra replay, falsificação, duplicatas e abuso.
- TLS, gestão de segredos, rate limits, auditoria e atualizações de dependências.
- Políticas de retenção e exclusão; adequação à LGPD.
- Testes de isolamento entre empresas e acompanhamento de acesso a histórico.

Nunca versionar `.env` real. Valores do `.env.example` devem servir apenas para desenvolvimento local. Não publicar a API sem controles.
