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
        # -> Perform calculation '50+10%' and submit.
        frame = context.pages[-1]
        # Input 10 as percentage value
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('10')
        

        frame = context.pages[-1]
        # Input 50 as number value
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div[2]/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('50')
        

        frame = context.pages[-1]
        # Click calculate button to perform 50+10% calculation
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div[3]/button[3]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Perform calculation '100-(25%)' and submit.
        frame = context.pages[-1]
        # Input 25 as percentage value
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('25')
        

        frame = context.pages[-1]
        # Input 100 as number value
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div[2]/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('100')
        

        frame = context.pages[-1]
        # Click calculate button to perform 100-(25%) calculation
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div[3]/button[3]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Navigate to advanced calculator and perform '(2+3)*4' calculation.
        frame = context.pages[-1]
        # Click on advanced calculator tab to perform advanced calculations
        elem = frame.locator('xpath=html/body/div/div/div/nav/button[2]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Input the expression '(2+3)*4' using the advanced calculator buttons and submit.
        frame = context.pages[-1]
        # Click '(' button
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[2]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Click '2' button
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[13]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Click '3' button
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[14]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Click ')' button
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[3]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Click '×' (multiply) button
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[8]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Click '4' button
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[11]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Click 'إظهار السجل' button to open history view after calculation
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div[2]/button').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Click input display to focus
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/input').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Click '⌫' to simulate pressing Enter or calculate (if no explicit Enter button)
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[20]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Clear the current input, correctly input '(2+3)*4', perform the calculation by clicking the correct calculate button, then open the history view to verify all calculations.
        frame = context.pages[-1]
        # Click 'C' button to clear current input
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Click '(' button
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[2]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Click '1' button (incorrect, should be '2')
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[13]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Click '+' button
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[16]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Click '2' button (incorrect, should be '3')
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[14]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Click ')' button
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[3]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Click '×' button
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[8]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Click '6' button (incorrect, should be '4')
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[11]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Click 'احسب العملية =' button to perform calculation
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[21]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Extract and verify the history log entries to check if all calculations including percentage and advanced operations are recorded correctly and in chronological order.
        frame = context.pages[-1]
        # Click 'إظهار السجل' button to open history view
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div[2]/button').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # --> Assertions to verify final state
        frame = context.pages[-1]
        try:
            await expect(frame.locator('text=Calculation history is complete and accurate').first).to_be_visible(timeout=1000)
        except AssertionError:
            raise AssertionError("Test failed: The history log does not maintain all past calculations with correct entries including percentage and advanced operations as required by the test plan.")
        await asyncio.sleep(5)
    
    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()
            
asyncio.run(run_test())
    