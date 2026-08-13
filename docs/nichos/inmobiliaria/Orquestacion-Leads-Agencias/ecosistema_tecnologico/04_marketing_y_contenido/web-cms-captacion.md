# Web, CMS y captación propia

**Corte:** agosto de 2026 · **Ámbito:** España · agencia inmobiliaria extendida  
**Categoría:** Web / CMS / formularios / microsites de CRM

---

## 1. Función principal

Dar presencia de marca, SEO local y un canal propio de captación (formularios, chat, llamadas) independiente o complementario de los portales. En muchas agencias la web es escaparate; en otras es el front del CRM (Witei, Inmovilla y similares publican inventario en sitio propio).

---

## 2. Usuarios

| Rol | Uso |
|-----|-----|
| Titular / marketing | Contenidos, SEO, landings |
| Agente | Actualización de fichas (si el CMS no está ligado al CRM) |
| Admin CRM | Publicación automática inventario → web |
| Proveedor web / freelance | WordPress, hosting, formularios |

---

## 3. Momento del flujo

Captación de demanda y de propietarios; soporte a campañas ads (landing); branding continuo. No es el sistema de registro operativo (salvo que el CRM genere la web).

---

## 4. Información gestionada

- Páginas corporativas, blog, legal (aviso, privacidad, cookies)
- Inventario publicado (fotos, precio, tipología, referencia)
- Formularios (contacto, valoración, alerta de búsqueda)
- Cookies / consent mode; IDs de analítica
- Leads hacia email o CRM

---

## 5. Integraciones (tipo)

| Conexión | Tipo | Notas |
|----------|------|-------|
| CRM → web (Witei, Inmovilla, etc.) | Nativa | Inventario y formularios en el mismo ecosistema |
| WordPress / CMS genérico ↔ CRM | API / automatización / plugin / manual | Calidad desigual; muchos leads solo a email |
| Formularios (Gravity, Typeform, nativos) → CRM | API / automatización / email | Email = manual de facto |
| Portales | Manual o export CRM | Web propia ≠ feed portal |
| WhatsApp click-to-chat | Nativa (widget) | Conversación fuera del CRM |
| GA4 / GTM / Search Console | Nativa / script | Ver ficha analítica |

---

## 6. Flujo de datos (ASCII)

```text
Inventario CRM ──nativa/API──► Web (CMS o site CRM)
                                 │
Visitante ──formulario/WhatsApp──┤
                                 ▼
                    Email agente  /  CRM lead
                                 │
                                 ▼
                         Seguimiento humano
```

---

## 7. Limitaciones y tareas humanas

- Microagencias: webs estáticas o plantillas CRM poco mantenidas; SEO irregular. **[Media]**
- Duplicidad ficha web vs portal (precio/estado desactualizado).
- Formularios sin consentimiento explícito o sin registro en CRM.
- Capacidad anunciada de “web + CRM integrados” ≠ uso diario si los agentes publican solo en portales.
- Cumplimiento cookies (AEPD) y LSSI en captación por email: tareas humanas/jurídicas frecuentes.

---

## 8. Costes (solo públicos)

| Concepto | Dato | Fuente |
|----------|------|--------|
| WordPress (software) | GPL / sin licencia de producto | wordpress.org · **[Alta]** |
| Hosting / dominio / tema premium | no público homogéneo (mercado hosting) | — |
| Web incluida en CRM | Suele ir en plan SaaS; Inmovilla Full **79 €/mes** (hasta 7 usuarios; no desglosa “web”) | [Inmovilla](https://inmovilla.com/precios/) · **[Alta]** |
| Witei | Freemium + planes de pago; importes en web variables/promocionales | [Witei precios](https://get.witei.com/es/precios-crm/) · **[Media]** |
| Desarrollo a medida | no público / bajo presupuesto | — |

---

## 9. Competencia / enfoques comparados

| Enfoque | Ventaja | Fricción |
|---------|---------|----------|
| Web generada por CRM vertical | Sync inventario; menos doble entrada | Menos diseño/SEO libre; lock-in |
| WordPress + plugins inmobiliarios | Flexibilidad marca y contenidos | Integración CRM frágil; mantenimiento |
| Landing solo para ads | Conversión de campaña | No sustituye marca ni SEO |
| Solo ficha en portales (sin web propia) | Coste bajo | Dependencia total del portal; marca débil |

CNMC: Idealista/Fotocasa = plataformas de anuncios; la web de agencia compite por atención pero no desplaza el rol del portal. **[Alta]** · [CNMC](https://www.cnmc.es/sites/default/files/3831141.pdf)

---

## 10. Adopción + confianza

| Arquetipo | Adopción | Confianza |
|-----------|----------|-----------|
| Mediana / franquicia | Habitual (web marca + formularios) | Media |
| Micro | Habitual-baja (plantilla CRM o WordPress básico; a veces solo portales) | Baja |
| Web como canal #1 de leads vs portales | Poco frecuente como #1 | Media-baja |

Sin censo oficial de “% agencias con web propia activa”. **[Alta sobre el hueco]**

---

## 11. Madurez + justificación

**Digitalizada:** la mayoría con presencia web alguna.  
**Automatizada** solo cuando el CRM alimenta fichas y leads sin email intermedio.  
Uso típico España: **Digitalizada**, con automatización parcial en stacks CRM-web. **[Media]**

---

## 12. Validación

| Ítem | Estado |
|------|--------|
| Precios Inmovilla / modelo Witei | Documentados (ver fuentes) |
| % leads vía web propia vs portal | Pendiente |
| Calidad media de sync WordPress↔CRM | Cualitativa; sin encuesta |
| Cumplimiento cookies en muestra de webs | Pendiente |

---

← [Herramientas marketing](herramientas-marketing.md) | [Índice](../README.md) | [Siguiente: Analítica →](analitica-web.md)
