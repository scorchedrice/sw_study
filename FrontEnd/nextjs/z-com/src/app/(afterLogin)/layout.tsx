import {ReactNode} from 'react'
import style from '@/app/(afterLogin)/layout.module.css'
import Link from 'next/link'
import Image from 'next/image'
import zlogo from '../../../public/zlogo.png'

import NavMenu from './_component/navMenu'
import LogoutButton from './_component/LogoutButton'

type Props = {children : ReactNode}

export default function AfterLoginLayout({children}: Props) {
    return (
        <div className={style.container}>
            <header className={style.leftSectionWrapper}>
                <section className={style.leftSection}>
                    <div className={style.leftSectionFixed}>
                        <Link className={style.logo} href='/home'>
                            <div className={style.logoPill}>
                                <Image src={zlogo} alt={'z-com'} width={40} height={40} />
                            </div>
                        </Link>
                        <nav>
                            <ul>
                                <NavMenu/>
                                <Link href="/compose/tweet" className={style.postButton}>게시하기</Link>
                            </ul>
                        </nav>
                        <LogoutButton/>
                    </div>
                </section>
            </header>
            <div className={style.rightSectionWrapper}>
                <div className={style.rightSectionInner}>
                    <main className={style.main}>{children}, mainSection</main>
                    <section className={style.rightSection}>
                        RightSection
                        <form className={style.search}>
                            <input type="search" />
                        </form>
                    </section>
                </div>
            </div>
        </div>

    );
}