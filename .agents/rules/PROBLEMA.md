# Problema activo

Ancla corta del proyecto. Detalle de oferta: [Servicio profesional — Sprint de Orquestación de Leads](../../docs/nichos/inmobiliaria/Orquestacion-Leads-Agencias/Oferta/Ofertas/Servicio-Profesional.md).

## Quién

**ICP-01:** agencia residencial independiente en España, 3–20 agentes, CRM activo, más de un canal de demanda, responsable de CRM/ops y dirección con autonomía de compra.

## Dolor

Los leads entran por portal, web, email u otros canales; la conversación cambia de canal y el resultado no siempre vuelve al CRM. Aparecen:

- respuesta tardía o seguimiento abandonado tras el primer intento;
- consultas sin dueño o sin SLA;
- duplicados, datos insuficientes y actividad fuera del registro;
- fragmentación entre CRM, email, WhatsApp y hojas de cálculo.

Dolores de referencia: **D07** (respuesta tardía), **D19** (fragmentación), **D20** (automatización parcial). Adyacentes: D02, D08 — sin prometer mejorar la intención del lead ni toda la comunicación de la operación.

## Promesa (resultado que se vende)

Cada lead del alcance queda en el CRM con:

1. origen e identidad mínimos;
2. responsable y SLA interno;
3. siguiente acción;
4. escalado o reasignación si se incumple la regla;
5. resultado trazable — medido antes/después.

El cliente compra un **resultado operativo medible**, no horas de programación ni “IA”.

## Métricas de éxito

- Tiempo de primera respuesta / asignación.
- % de leads con owner.
- % de leads con siguiente acción definida.
- Cola de excepciones (datos insuficientes, fallos de sync, SLA incumplido).
- Baseline acordado vs. medición post-implantación.

## Fuera de alcance (ahora)

- Bot autónomo de ventas o scoring discriminatorio.
- Captación, compra de leads o campañas de marketing.
- Sustituir o migrar el CRM del cliente.
- Cobertura universal de WhatsApp personal, voz y todos los portales.
- Expediente, KYC/AML, firma, pagos, notaría.
- SaaS horizontal / multi-tenant como primer producto.
- Vender la plataforma multiagente interna como producto al cliente.
- Ampliar fases 2–6 de plataforma interna (knowledge completo, tools, memoria, orquestación de empresa, n8n) salvo que desbloqueen el sprint.

## Laboratorio técnico de este repo

Dashboard + API con **HubSpot** (Private App) es el **CRM activo de validación**: orquestación (dedupe, owner, SLA, excepciones, métricas) en local vía `/leads/ingest` y panel Leads.

- **Este repo (dev):** HubSpot — no requiere cuenta Witei.
- **Entrega a cliente ICP-01 en España:** CRM del cliente (Witei, Inmovilla, etc.); ver investigación de mercado, no este laboratorio.

El stack no redefine el problema.
