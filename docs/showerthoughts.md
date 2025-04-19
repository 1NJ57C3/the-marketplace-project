# showerthoughts.md - musings and rants, chaotic tangents and rabbit holes

This is where I try to capture random useful things that pop into my head for later... Or something.

## sessions/tokens management - 2025.04.18 - tangent.trigger: sliding tokens

> Ideally, the session manager should show the user the devices their tokens are synced to, when the token was last active, as well as origin date and location (or IP). With this information, the user should be able to make a well-informed choice as to which tokens they'd like to revoke, if not all of them. I guess if a token was stolen, though, even the rotating system won't likely mitigate the attack, nor really do very much in damage control.
>
> Most of these attacks happen rather quickly, so if the attacker knew what they were doing, it'd likely be out of our control, and require manual intervention by someone with `is_staff` perms. In the optimal case, in which the user wasn't locked out of their account in time, they could retaliate by nuking tokens and changing their passwords. We can write a "change your password" prompt to pair with "log out of all devices", but there's a good chance that this backfires and allows attackers to more easily get to lock the user out by streamlining the password change flow, although if UX is good, there should be no difficulty accessing this either way. "Log out of all devices" can also issue a brand new token on the spot while deactivating all other tokens at once, so that the user still has continuous access. However, if we track rotating tokens, we might have some visibility on warning signs.
>
> All of this will more than likely require fingerprinting, which adds complexity that may be too high at this stage of the project, but we can always side-quest it.
