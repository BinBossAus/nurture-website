"use client";

import { useRef } from "react";
import gsap from "gsap";
import { useGSAP } from "@gsap/react";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { SHOTS, type Shot } from "@/lib/shots";

gsap.registerPlugin(useGSAP);
if (typeof window !== "undefined") {
  gsap.registerPlugin(ScrollTrigger);
}

function PearMark() {
  return (
    <svg
      className="hero-mark"
      viewBox="0 0 18 22"
      aria-hidden="true"
      fill="currentColor"
    >
      <path d="M9.1 1.2c.7 1.4.8 2.5.1 3.4C6.6 5.5 4.4 8.2 4.4 11.6c0 3 2 5.2 4.7 5.2s4.7-2.2 4.7-5.2c0-3.4-2.2-6.1-4.8-7-.7-.9-.6-2 .1-3.4Z" />
      <path
        d="M9.3.6c.12 1.4 0 2.4-.5 3.2"
        fill="none"
        stroke="currentColor"
        strokeWidth="1.1"
        strokeLinecap="round"
        opacity="0.7"
      />
    </svg>
  );
}

function ShotLayer({ shot, on }: { shot: Shot; on?: boolean }) {
  const hasPortrait = Boolean(shot.srcPortrait);

  return (
    <div
      className={
        (hasPortrait ? "hero-shot hero-has-portrait" : "hero-shot") +
        (on ? " is-on" : "")
      }
      data-shot={shot.id}
    >
      <div className="hero-media" style={{ transformOrigin: shot.origin }}>
        <video
          className={
            hasPortrait ? "hero-video hero-video-landscape" : "hero-video"
          }
          src={shot.src}
          poster={shot.poster}
          muted
          loop
          playsInline
          autoPlay
          preload="auto"
          style={{ objectPosition: shot.position }}
        />
        {hasPortrait ? (
          <video
            className="hero-video hero-video-portrait"
            src={shot.srcPortrait}
            poster={shot.posterPortrait ?? shot.poster}
            muted
            loop
            playsInline
            autoPlay
            preload="auto"
            style={{
              objectPosition: shot.positionPortrait ?? shot.position,
            }}
          />
        ) : null}
      </div>
    </div>
  );
}

function buildBeats(
  shots: HTMLElement[],
  medias: Array<HTMLElement | null>,
  fill: HTMLElement | null,
  hint: HTMLElement | null,
) {
  const tl = gsap.timeline({ paused: true, defaults: { ease: "none" } });

  gsap.set(shots, { opacity: 0 });
  gsap.set(shots[0], { opacity: 1 });
  gsap.set(medias, { scale: 1 });
  gsap.set(medias[0], { scale: 1.06 });

  if (fill) {
    tl.fromTo(fill, { scaleX: 0 }, { scaleX: 1, duration: 10 }, 0);
  }
  if (hint) {
    tl.to(hint, { opacity: 0, duration: 0.4 }, 0.08);
  }

  // Stage 1 — brief macro of the hand (not the whole hero)
  tl.to(medias[0], { scale: 1.02, duration: 0.9 }, 0);

  // Stage 2 — complete girl from behind, reaching into the tree
  tl.to(shots[0], { opacity: 0, duration: 0.55 }, 0.95);
  tl.fromTo(shots[1], { opacity: 0 }, { opacity: 1, duration: 0.55 }, 0.95);
  tl.fromTo(medias[1], { scale: 1.04 }, { scale: 1, duration: 0.55 }, 0.95);
  tl.to(medias[1], { scale: 1, duration: 2.35 }, 1.5);

  // Stage 3 — wider orchard
  tl.to(shots[1], { opacity: 0, duration: 0.6 }, 3.7);
  tl.fromTo(shots[2], { opacity: 0 }, { opacity: 1, duration: 0.6 }, 3.7);
  tl.fromTo(medias[2], { scale: 1.08 }, { scale: 1, duration: 1.7 }, 3.7);

  // Stage 4 — canopy
  tl.to(shots[2], { opacity: 0, duration: 0.6 }, 5.4);
  tl.fromTo(shots[3], { opacity: 0 }, { opacity: 1, duration: 0.6 }, 5.4);
  tl.fromTo(medias[3], { scale: 1.1 }, { scale: 1, duration: 1.65 }, 5.4);

  // Stage 5 — home, full girl again
  tl.to(shots[3], { opacity: 0, duration: 0.6 }, 7.15);
  tl.fromTo(shots[4], { opacity: 0 }, { opacity: 1, duration: 0.6 }, 7.15);
  tl.fromTo(medias[4], { scale: 1.04 }, { scale: 1, duration: 2.25 }, 7.15);

  return tl;
}

function shotIndex(progress: number) {
  if (progress >= 0.72) return 4;
  if (progress >= 0.54) return 3;
  if (progress >= 0.37) return 2;
  if (progress >= 0.12) return 1;
  return 0;
}

export function HeroJourney() {
  const rootRef = useRef<HTMLElement>(null);
  const scrollRef = useRef<HTMLDivElement>(null);

  // NOTE: video playback is armed/synced from inside the useGSAP hook below,
  // which only plays the on-screen shot's video(s) and pauses the rest. Do
  // NOT add a blanket "play every video" effect here — with 7 <video>
  // elements on the page, forcing them all to play at once (as a previous
  // version of this effect did on an interval) makes every browser decode
  // all 7 HD streams simultaneously, which is heavy enough to visibly stall
  // scroll-driven rendering (the "stuck on one scene" symptom).

  useGSAP(
    () => {
      const root = rootRef.current;
      const scroller = scrollRef.current;
      if (!root || !scroller) return;

      const shots = gsap.utils.toArray<HTMLElement>("[data-shot]", root);
      const medias = shots.map((shot) =>
        shot.querySelector<HTMLElement>(".hero-media"),
      );
      const fill = root.querySelector<HTMLElement>(".hero-progress-fill");
      const hint = root.querySelector<HTMLElement>(".hero-hint");
      const dots = gsap.utils.toArray<HTMLElement>("[data-dot]", root);

      const reduce = window.matchMedia(
        "(prefers-reduced-motion: reduce)",
      ).matches;

      const setActive = (index: number) => {
        dots.forEach((dot, i) => {
          dot.classList.toggle("is-active", i === index);
        });
      };

      const syncVideos = () => {
        for (const shot of shots) {
          const opacity = Number.parseFloat(
            window.getComputedStyle(shot).opacity,
          );
          const live = opacity > 0.05;
          shot
            .querySelectorAll<HTMLVideoElement>("video")
            .forEach((video) => {
              // Only decode the variant CSS is actually showing (landscape
              // vs. portrait) — the hidden one shouldn't be playing either.
              const hidden =
                window.getComputedStyle(video).display === "none";
              const shouldPlay = live && !hidden;
              if (shouldPlay) {
                if (video.paused) void video.play().catch(() => undefined);
              } else if (!video.paused) {
                video.pause();
              }
            });
        }
      };

      if (reduce) {
        gsap.set(shots, { opacity: 0 });
        gsap.set(shots[1] ?? shots[0], { opacity: 1 });
        gsap.set(medias, { scale: 1 });
        setActive(1);
        syncVideos();
        const onInteractReduced = () => syncVideos();
        window.addEventListener("pointerdown", onInteractReduced, {
          once: true,
        });
        return () => {
          window.removeEventListener("pointerdown", onInteractReduced);
        };
      }

      const tl = buildBeats(shots, medias, fill, hint);

      const apply = (progress: number) => {
        const p = Math.max(0, Math.min(1, progress));
        tl.progress(p);
        setActive(shotIndex(p));
        syncVideos();
      };

      apply(0);

      let mode: "auto" | "scroll" = "auto";
      const stage2 = 0.28;

      const introProxy = { p: 0 };
      const intro = gsap.to(introProxy, {
        p: stage2,
        duration: 3.4,
        delay: 1.35,
        ease: "power1.inOut",
        onUpdate() {
          if (mode !== "auto") return;
          apply(introProxy.p);
        },
      });

      const st = ScrollTrigger.create({
        trigger: scroller,
        start: "top top",
        end: "bottom bottom",
        scrub: 0.75,
        invalidateOnRefresh: true,
        onUpdate(self) {
          if (self.progress > 0.012 || Math.abs(self.getVelocity()) > 40) {
            if (mode !== "scroll") {
              mode = "scroll";
              intro.kill();
            }
          }
          if (mode === "scroll") apply(self.progress);
        },
      });

      const onResize = () => ScrollTrigger.refresh();
      window.addEventListener("resize", onResize);
      window.addEventListener("load", onResize);

      // Some mobile browsers block the initial programmatic autoplay until
      // the very first user gesture. Re-run the (visibility-aware) sync once
      // on first touch/click so the active shot's video starts, without
      // ever forcing the other, off-screen videos to play too.
      const onFirstInteraction = () => syncVideos();
      window.addEventListener("pointerdown", onFirstInteraction, {
        once: true,
      });
      window.addEventListener("touchstart", onFirstInteraction, {
        once: true,
        passive: true,
      });

      return () => {
        intro.kill();
        st.kill();
        tl.kill();
        window.removeEventListener("resize", onResize);
        window.removeEventListener("load", onResize);
        window.removeEventListener("pointerdown", onFirstInteraction);
        window.removeEventListener("touchstart", onFirstInteraction);
      };
    },
    { scope: rootRef },
  );

  return (
    <main
      ref={rootRef}
      className="relative bg-espresso text-ivory"
      aria-label="Cinematic orchard sequence"
    >
      <h1 className="sr-only">Nurture</h1>
      <div ref={scrollRef} className="hero-scroll">
        <div className="hero-stage">
          {SHOTS.map((shot, index) => (
            <ShotLayer key={shot.id} shot={shot} on={index === 0} />
          ))}
          <div className="hero-vignette" />
          <div className="hero-grain" />
          <div className="hero-progress" aria-hidden="true">
            <span className="hero-progress-fill" />
          </div>
          <div className="hero-dots" aria-hidden="true">
            {SHOTS.map((shot, index) => (
              <span
                key={shot.id}
                data-dot={shot.id}
                className={index === 0 ? "hero-dot is-active" : "hero-dot"}
              />
            ))}
          </div>
          <div className="hero-hint" aria-hidden="true">
            <span className="hero-chevron" />
            <span className="hero-chevron" />
          </div>
          <PearMark />
        </div>
      </div>
    </main>
  );
}
