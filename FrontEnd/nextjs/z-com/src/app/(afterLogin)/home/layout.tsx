import { ReactNode } from "react";

type Props = {
    children: ReactNode
}

export default async function HomeLayout({children}: { children: ReactNode }) {
    return (
        <div>
            홈 레이아웃
            {children}
        </div>
    );
}