# showerthoughts.md - musings and rants, chaotic tangents and rabbit holes

This is where I try to capture some of the useful chaos that pop into my head for later... Or something.

## sessions/tokens management - 2025.04.18 - tangent.trigger: sliding tokens

> Ideally, the session manager should show the user the devices their tokens are synced to, when the token was last active, as well as origin date and location (or IP). With this information, the user should be able to make a well-informed choice as to which tokens they'd like to revoke, if not all of them. I guess if a token was stolen, though, even the rotating system won't likely mitigate the attack, nor really do very much in damage control.
>
> Most of these attacks happen rather quickly, so if the attacker knew what they were doing, it'd likely be out of our control, and require manual intervention by someone with `is_staff` perms. In the optimal case, in which the user wasn't locked out of their account in time, they could retaliate by nuking tokens and changing their passwords. We can write a "change your password" prompt to pair with "log out of all devices", but there's a good chance that this backfires and allows attackers to more easily get to lock the user out by streamlining the password change flow, although if UX is good, there should be no difficulty accessing this either way. "Log out of all devices" can also issue a brand new token on the spot while deactivating all other tokens at once, so that the user still has continuous access. However, if we track rotating tokens, we might have some visibility on warning signs.
>
> All of this will more than likely require fingerprinting, which adds complexity that may be too high at this stage of the project, but we can always side-quest it.

---

<!-- // commenting/editing for showerthoughts.md use, now that I'm back from Cat DMs. -->
<!-- // thisisforme - -->

## 2025.04.19 noonish - tangent.trigger: 'change_password' flow => file structure

>Before we do, we can probably come up with a further optimized solution. If we think about further polishing auth and/or stretch goals on our radar, we've got what? `User` patching, change of password (this), forgotten password, email verification (registration, etc.), OAuth/social auth, token fingerprinting (mega-stretch-goal),  
>
>*/\* lightbulb moment -- I really should just build out the project's MVP, this project will still be malleable later, so we can swap out and improve whatever parts we have ideas for. Parts of it might look like spaceship, whilst other parts might stay looking like dirt huts in starting MineCraft, and that's okay. <!-- (interrupted for about 20 minutes because Cat DMs; talking college/housing) --> \*/*  
>
>// rereading what we have so far *again*, trying to recapture the thought  
>
>...client-executed token revocation (might actually be done-ish; [blacklist] setup?)  
>
><!-- // 1:45p -- Probably sobered up (losing focus). Took approx 20-25mg THC noonish (St. Ides Mango) -- noticeably back to rapid subconscious thought streams -- back to hitting Stiiizy again, we'll see   -->
>
>...Seems that train of thought's cooked.  
>
>Nope!  
>
>...forgotten username, login using *either* username or email, email confirmations (email/password changes, etc.) aaaand... That's all the missing auth backend I can think of for now.  
>
>A little less than half of these would probably benefit from being decoupled from the others. Would it make more sense to group these by categorical function, rather than individual feature? Or am I just splitting hairs? I like the idea of higher modularity, but am concerned about background cognitive costs.  

---

## 2025.04.19 / 2:10p - tangent.last().resolution

>I think we should go with per-feature modularity, after all. It'll be easier to swap things in and out if we find better solutions later. Hypothetically, it'll also simplify onboarding for our audience of n(one). It's easier for me to navigate flow by directory than to chase organizational flow in a large file if I don't know *specifically* what to look for by name.

---

## 2025.04.20 / 1:30p - tangent.trigger: switching to TDD for flexible login (using username or email address)

>Is there any value in writing a test template parser/generator? Like a package that allows the user to write their tests in (mostly) plain English? Something loosely like this, for example?
>
>testGen('logging in with the username "assface" and password "whatsapassword" should not return a token', 'users/auth/tests/test_login.py'); => test file
>
>Or maybe make it a shell executable that prompts the user for the necessary variable values?
