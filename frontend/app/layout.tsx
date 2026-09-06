import type { ReactNode } from "react";

export const metadata = {
  title: "PR Campaign Copilot",
  description: "Explainable PR targeting and outreach strategy.",
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
