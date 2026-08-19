## Supply-chain hardening (frontend)

Regla de cutoff:

- Para actualizar dependencias del frontend, **solo se aceptan versiones publicadas antes del 2026-08-01**.
- El objetivo es reducir riesgo de supply-chain. No existe una prueba “universal” de malware, pero el cutoff + version pinning minimiza cambios inesperados.

Cómo aplicar la regla:

1. **Pinear versiones exactas** en `frontend/package.json`.
   - Prohibido usar rangos con `^` o `~`.
   - Se debe usar formato `"<version>"` exacto.
2. **Verificar fecha de publicación** antes de hacer `npm install`:
   - Ejecuta (para cada paquete que vayas a cambiar):
     - `npm view <package>@<version> time`
   - Confirma que la fecha esté **antes de 2026-08-01**.
3. Generar y usar lockfile:
   - Regenerar `frontend/package-lock.json` con `npm install --no-audit --no-fund`.
   - En CI/entornos reproducibles, usar `npm ci`.
4. Auditoría rápida:
   - Ejecutar `npm audit --production` (si aplica) y documentar resultados.

Estado actual:

- Las dependencias del proyecto ya están pinneadas a versiones exactas en `frontend/package.json`.

