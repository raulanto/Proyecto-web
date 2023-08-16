<template>
    <nav class="flex justify-between items-center text-sm font-medium my-3 px-6">
        <a href="text-" class="underline">showing 267 search results</a>
        <div class="flex mx-1">
            <div class="flex relative mx-1 items-center">
                <h1 class="mr-3">Map View</h1>
                <label for="check1" class=" cursor-pointer relative w-12 h-6 rounded-full">
                    <input type="checkbox" id="check1" class="sr-only peer">
                    <div class="box bg-gray-200 block h-6 w-12 rounded-full peer-checked:bg-green-200"></div>
                    <span
                        class="w-2/5 h-4/5 bg-gray-600 absolute rounded-full left-1 top-0.5 peer-checked:bg-green-700 peer-checked:left-6 transition-all duration-500"></span>
                </label>


            </div>

            <div class="flex relative mx-1 items-center">
                <h5 class="mr-3">Verified Only</h5>
                <label for="check" class=" cursor-pointer relative w-12 h-6 rounded-full">
                    <input type="checkbox" id="check" class="sr-only peer">
                    <div class="box bg-gray-200 block h-6 w-12 rounded-full peer-checked:bg-green-200"></div>
                    <span
                        class="w-2/5 h-4/5 bg-gray-600 absolute rounded-full left-1 top-0.5 peer-checked:bg-green-700 peer-checked:left-6 transition-all duration-500"></span>
                </label>



            </div>
            <button
                class="border rounded-md px-3 p-1 mx-1 text-center flex items-center hover:bg-gray-100 transition-all duration-200">
                <span class="material-symbols-outlined scale-[.7] ">
                    page_info
                </span>Filter</button>
            <button class="border rounded-md px-3 p-1 mx-1 flex items-center hover:bg-gray-100 transition-all duration-200">
                <span class="material-symbols-outlined scale-[.7]">
                    menu
                </span> Sort by
            </button>
        </div>

    </nav>
</template>