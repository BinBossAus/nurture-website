export type Shot = {
  id: string;
  src: string;
  srcPortrait?: string;
  poster: string;
  posterPortrait?: string;
  position: string;
  positionPortrait?: string;
  origin: string;
};

export const SHOTS: Shot[] = [
  {
    id: "close",
    src: "/hero/close.mp4",
    poster: "/hero/close.jpg",
    position: "70% 48%",
    origin: "70% 48%",
  },
  {
    id: "reach",
    src: "/hero/reach-wide.mp4",
    srcPortrait: "/hero/reach-portrait.mp4",
    poster: "/hero/reach-wide.jpg",
    posterPortrait: "/hero/source.jpg",
    position: "40% 58%",
    positionPortrait: "50% 55%",
    origin: "42% 62%",
  },
  {
    id: "orchard",
    src: "/hero/orchard.mp4",
    poster: "/hero/orchard.jpg",
    position: "50% 78%",
    origin: "50% 72%",
  },
  {
    id: "canopy",
    src: "/hero/canopy.mp4",
    poster: "/hero/canopy.jpg",
    position: "50% 48%",
    origin: "50% 45%",
  },
  {
    id: "home",
    src: "/hero/reach-wide.mp4",
    srcPortrait: "/hero/reach-portrait.mp4",
    poster: "/hero/reach-wide.jpg",
    posterPortrait: "/hero/source.jpg",
    position: "40% 58%",
    positionPortrait: "50% 55%",
    origin: "42% 60%",
  },
];
