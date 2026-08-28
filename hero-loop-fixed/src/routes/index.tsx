import { createFileRoute } from "@tanstack/react-router";
import { HeroJourney } from "@/components/hero-journey";

export const Route = createFileRoute("/")({ component: Home });

function Home() {
  return <HeroJourney />;
}
