import React from 'react';
import { Link } from 'react-router-dom';
import Footer from '../Footer';

export default function LayoutDefault({ children }) {
    return (
        <body>
            <div className="relative isolate overflow-hidden bg-white px-6 py-24 sm:py-32 lg:overflow-visible lg:px-0">
                <div className="absolute inset-0 -z-10 overflow-hidden">
                    <svg
                        className="absolute left-[max(50%,25rem)] top-0 h-[64rem] w-[128rem] -translate-x-1/2 stroke-gray-200 [mask-image:radial-gradient(64rem_64rem_at_top,white,transparent)]"
                        aria-hidden="true"
                    >
                        <defs>
                            <pattern
                                id="e813992c-7d03-4cc4-a2bd-151760b470a0"
                                width="200"
                                height="200"
                                x="50%"
                                y="-1"
                                patternUnits="userSpaceOnUse"
                            >
                                <path d="M100 200V.5M.5 .5H200" fill="none" />
                            </pattern>
                        </defs>
                        <svg x="50%" y="-1" className="overflow-visible fill-gray-50">
                            <path
                                d="M-100.5 0h201v201h-201Z M699.5 0h201v201h-201Z M499.5 400h201v201h-201Z M-300.5 600h201v201h-201Z"
                                strokeWidth="0"
                            />
                        </svg>
                        <rect
                            width="100%"
                            height="100%"
                            strokeWidth="0"
                            fill="url(#e813992c-7d03-4cc4-a2bd-151760b470a0)"
                        />
                    </svg>
                </div>
                <div className="mx-auto grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 lg:mx-0 lg:max-w-none lg:grid-cols-2 lg:items-start lg:gap-y-10">
                    <div className="lg:col-span-2 lg:col-start-1 lg:row-start-1 lg:mx-auto lg:grid lg:w-full lg:max-w-7xl lg:grid-cols-2 lg:gap-x-8 lg:px-8">
                        <div className="lg:pr-4">
                            <div className="lg:max-w-lg">
                                <p className="flex gap-2 text-base font-semibold leading-7 text-indigo-600">
                                    <Link to="#" className="hover:underline">
                                        #voice
                                    </Link>
                                    <Link to="#" className="hover:underline">
                                        #machine-learning
                                    </Link>
                                    <Link to="#" className="hover:underline">
                                        #ai
                                    </Link>
                                    <Link to="#" className="hover:underline">
                                        #recognition
                                    </Link>
                                </p>
                                <h1 className="mt-2 line-clamp-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
                                    Voice Recognition Web Application
                                </h1>
                                <p className="mt-6 text-xl leading-8 text-gray-700">
                                    Voice recognition, or speech recognition, is advanced technology that translates
                                    spoken language into text, enabling hands-free interaction with devices. Widely used
                                    in virtual assistants and smart devices, it enhances user experience and
                                    accessibility, with ongoing advancements driving its evolution in the digital
                                    landscape.
                                </p>
                            </div>
                        </div>
                    </div>
                    <div className="-ml-12 -mt-12 p-12 lg:sticky lg:top-4 lg:col-start-2 lg:row-span-2 lg:row-start-1 lg:overflow-hidden">
                        <img
                            className="w-[48rem] max-w-none rounded-2xl bg-gray-900 shadow-xl ring-1 ring-gray-400/10 sm:w-[57rem]"
                            src="https://images.unsplash.com/photo-1558539090-4456a2cc9fba?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDR8fHZvaWNlJTIwcmVjb2duaXRpb258ZW58MHx8MHx8fDA%3D"
                            alt=""
                        />
                    </div>
                    {/* HERE! */}
                    <div className="lg:col-span-2 lg:col-start-1 lg:row-start-2 lg:mx-auto lg:grid lg:w-full lg:max-w-7xl lg:grid-cols-2 lg:gap-x-8 lg:px-8">
                        <div className="lg:pr-4">
                            <div className="max-w-xl text-base leading-7 text-gray-700 lg:max-w-lg">
                                {children}
                                <Footer />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </body>
    );
}
