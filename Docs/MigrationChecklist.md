# UE 5.7.4 Migration Checklist

- Keep project under an ASCII-only path.
- Regenerate project files after the UE update finishes.
- Build once from Visual Studio before opening the editor.
- Check `PawnSensingComponent` warnings. Replace with AI Perception only if the warning becomes an error.
- Recreate Blueprint classes that the source expects:
  - Player avatar Blueprint based on `APlayerAvatar`
  - Enemy Blueprint based on `AEnemy`
  - Defense tower Blueprint based on `ADefenseTower`
  - Health bar widget based on `UHealthBarWidget`
- Configure input actions:
  - `SetDestination`
  - `Attack`
- Import required assets from `PangaeaAssets`.
