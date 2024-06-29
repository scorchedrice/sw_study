"use client"

import style from "./navMenu.module.css"
import { useSelectedLayoutSegment } from "next/navigation"
import Link from 'next/link'

export default function navMenu() {
    const segment = useSelectedLayoutSegment()
    // 디렉토리 명을 알기 위함. 내가 어디있는지 알 수 있음.
    // 디테일하게 알고싶다면 useSelectedLayoutSegments() 사용
    console.log(segment)

    const me = {
        id: 'myID'
    }

    return (
        <div>
            <li>
                <Link href="/home">
                    <div>Home</div>
                </Link>
            </li>
            <li>
                <Link href="/explore">
                    <div>Explore</div>
                </Link>
            </li>
            <li>
                <Link href="/messages">
                    <div>Message</div>
                </Link>
            </li>
            <li>
                <Link href={`/{me}`}>
                    <div>Profile</div>
                </Link>
            </li>
        </div>
    )
}