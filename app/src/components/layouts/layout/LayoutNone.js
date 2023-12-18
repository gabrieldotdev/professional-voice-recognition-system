import sls from "./Layout.module.css";

export default function LayoutNone({ children }) {
    return (
        <div className="flex h-screen flex-col">
            <div className="flex flex-1 overflow-hidden">
                <main className={`${sls.border_dashed_zinc_600_2} flex flex-1 items-center justify-center`}>{children}</main>
            </div>
        </div>
    );
}
