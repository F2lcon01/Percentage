import asyncio
from playwright import async_api
from playwright.async_api import expect

async def run_test():
    pw = None
    browser = None
    context = None
    
    try:
        # Start a Playwright session in asynchronous mode
        pw = await async_api.async_playwright().start()
        
        # Launch a Chromium browser in headless mode with custom arguments
        browser = await pw.chromium.launch(
            headless=True,
            args=[
                "--window-size=1280,720",         # Set the browser window size
                "--disable-dev-shm-usage",        # Avoid using /dev/shm which can cause issues in containers
                "--ipc=host",                     # Use host-level IPC for better stability
                "--single-process"                # Run the browser in a single process mode
            ],
        )
        
        # Create a new browser context (like an incognito window)
        context = await browser.new_context()
        context.set_default_timeout(5000)
        
        # Open a new page in the browser context
        page = await context.new_page()
        
        # Navigate to your target URL and wait until the network request is committed
        await page.goto("http://localhost:8080", wait_until="commit", timeout=10000)
        
        # Wait for the main page to reach DOMContentLoaded state (optional for stability)
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=3000)
        except async_api.Error:
            pass
        
        # Iterate through all iframes and wait for them to load as well
        for frame in page.frames:
            try:
                await frame.wait_for_load_state("domcontentloaded", timeout=3000)
            except async_api.Error:
                pass
        
        # Interact with the page elements to simulate user flow
        # -> Perform calculation '5 + 10' and obtain result '15'.
        frame = context.pages[-1]
        # Input first number 5 for calculation
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('5')
        

        frame = context.pages[-1]
        # Input second number 10 for calculation
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div[2]/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('10')
        

        frame = context.pages[-1]
        # Click the calculate button to perform the calculation
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div[3]/button[3]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Switch to standard calculator mode to perform arithmetic calculations.
        frame = context.pages[-1]
        # Click the 'آلة حاسبة' (Calculator) button to switch to standard calculator mode
        elem = frame.locator('xpath=html/body/div/div/div/nav/button[2]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Complete the first calculation input by clicking '0', then click equals to perform the calculation, and verify the history log.
        frame = context.pages[-1]
        # Click number 0 to complete '5+10'
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[17]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Click equals button to perform the calculation
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[21]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Perform calculation '20 - 3' and verify result '17'.
        frame = context.pages[-1]
        # Click clear button to clear input for next calculation
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[20]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Click plus operator '+' to clear any residual input
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[16]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Click number 2
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[13]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Click number 3
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[15]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Click minus operator '-'
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[12]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Click number 3
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[15]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Click equals button to perform the calculation
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[21]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Click to show the history log to verify the new entry
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div[2]/button').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # --> Assertions to verify final state
        frame = context.pages[-1]
        try:
            await expect(frame.locator('text=Calculation History Verified Successfully').first).to_be_visible(timeout=1000)
        except AssertionError:
            raise AssertionError("Test case failed: The test plan execution has failed because the history log did not save completed calculations correctly and in sequence as required.")
        await asyncio.sleep(5)
    
    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()
            
asyncio.run(run_test())
    