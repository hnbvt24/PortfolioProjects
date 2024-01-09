/*

Cleaning the SQL Data

*/

Select *
From [PortfolioProject].[dbo].[NashvilleHousing]

-------------------------------------------------------------------------------------------------

-- Populate Property Address data

Select *
From [PortfolioProject].[dbo].[NashvilleHousing]
--Where PropertyAddress IS NULL
Order by ParcelID

Select nash1.ParcelID, nash1.PropertyAddress, nash2.ParcelID, nash2.PropertyAddress, ISNULL(nash1.PropertyAddress, nash2.PropertyAddress)
From [PortfolioProject].[dbo].[NashvilleHousing] nash1
JOIN [PortfolioProject].[dbo].[NashvilleHousing] nash2
    on nash1.ParcelID = nash2.ParcelID
    AND nash1.[UniqueID] <> nash2.[UniqueID]
Where nash1.PropertyAddress IS NULL

Update nash1
SET PropertyAddress = ISNULL(nash1.PropertyAddress, nash2.PropertyAddress)
From [PortfolioProject].[dbo].[NashvilleHousing] nash1
JOIN [PortfolioProject].[dbo].[NashvilleHousing] nash2
    on nash1.ParcelID = nash2.ParcelID
    AND nash1.[UniqueID] <> nash2.[UniqueID]
Where nash1.PropertyAddress IS NULL
-------------------------------------------------------------------------------------------------

-- Breaking out Address into Individual Columns (Address, City, State)

-- Let's start first with the Property Address, which has 1 comma we need to address and split out the city
Select PropertyAddress
From [PortfolioProject].[dbo].[NashvilleHousing]
--Where PropertyAddress IS NULL
--Order by ParcelID

Select 
    SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) -1) as Address,
    SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) +1, LEN(PropertyAddress)) as City
From [PortfolioProject].[dbo].[NashvilleHousing]

ALTER TABLE [PortfolioProject].[dbo].[NashvilleHousing]
Add PropertySplitAddress NVARCHAR(255);

Update [PortfolioProject].[dbo].[NashvilleHousing]
SET PropertySplitAddress = SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) -1)

ALTER TABLE [PortfolioProject].[dbo].[NashvilleHousing]
Add PropertySplitCity NVARCHAR(255);

Update [PortfolioProject].[dbo].[NashvilleHousing]
SET PropertySplitCity = SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) +1, LEN(PropertyAddress))

-- We can see our two new columns attached to the very end of the table
Select *
From [PortfolioProject].[dbo].[NashvilleHousing]

-- Now let's move on to the Owner Address, which has 2 commas we need to address and split out the city and the state as well
Select OwnerAddress
From [PortfolioProject].[dbo].[NashvilleHousing]

-- ParseName() looks for periods, so let's replace all commas with a period instead
Select 
PARSENAME(REPLACE(OwnerAddress, ',', '.'), 3),
PARSENAME(REPLACE(OwnerAddress, ',', '.'), 2),
PARSENAME(REPLACE(OwnerAddress, ',', '.'), 1)
From [PortfolioProject].[dbo].[NashvilleHousing]

-- Let's add those columns to our table
ALTER TABLE [PortfolioProject].[dbo].[NashvilleHousing]
Add OwnerSplitAddress NVARCHAR(255);

Update [PortfolioProject].[dbo].[NashvilleHousing]
SET OwnerSplitAddress = PARSENAME(REPLACE(OwnerAddress, ',', '.'), 3)

ALTER TABLE [PortfolioProject].[dbo].[NashvilleHousing]
Add OwnerSplitCity NVARCHAR(255);

Update [PortfolioProject].[dbo].[NashvilleHousing]
SET OwnerSplitCity = PARSENAME(REPLACE(OwnerAddress, ',', '.'), 2)

ALTER TABLE [PortfolioProject].[dbo].[NashvilleHousing]
Add OwnerSplitState NVARCHAR(255);

Update [PortfolioProject].[dbo].[NashvilleHousing]
SET OwnerSplitState = PARSENAME(REPLACE(OwnerAddress, ',', '.'), 1)

-------------------------------------------------------------------------------------------------

-- Change Y to N to Yes and No in "Sold as Vacant" field

Select Distinct(SoldAsVacant), Count(SoldAsVacant)
From [PortfolioProject].[dbo].[NashvilleHousing]
Group By SoldAsVacant
Order by 2

-- There's more Yes and No entries and we want to convert all other entries over to their equivalent

Select SoldAsVacant,
    CASE 
        When SoldAsVacant = 'Y' THEN 'Yes'
        When SoldAsVacant = 'N' THEN 'No'
        Else SoldAsVacant
    END
From [PortfolioProject].[dbo].[NashvilleHousing]

Update NashvilleHousing
SET SoldAsVacant = 
    CASE 
        When SoldAsVacant = 'Y' THEN 'Yes'
        When SoldAsVacant = 'N' THEN 'No'
        Else SoldAsVacant
    END

-------------------------------------------------------------------------------------------------

-- Remove Duplicates
WITH RowNumCTE AS(
    Select *,
    ROW_NUMBER() OVER (
        PARTITION BY ParcelID,
                     PropertyAddress,
                     SalePrice,
                     SaleDate,
                     LegalReference
                     ORDER BY 
                        UniqueID
    ) row_num
From [PortfolioProject].[dbo].[NashvilleHousing]
)
Delete
From RowNumCTE
Where row_num > 1

/* SWAP THIS OUT AFTER RUNNING DELETE STATMENT TO CONFIRM THE DUPLICATES HAVE BEEN DELETED SUCCESSFULLY
Select *
From RowNumCTE
Where row_num > 1
*/

-------------------------------------------------------------------------------------------------

-- Delete Unused Columns

Select *
From [PortfolioProject].[dbo].[NashvilleHousing]

ALTER TABLE [PortfolioProject].[dbo].[NashvilleHousing]
DROP COLUMN OwnerAddress, TaxDistrict, PropertyAddress, SaleDate


-------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------