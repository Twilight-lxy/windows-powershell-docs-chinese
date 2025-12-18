---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BitLocker-help.xml
Module Name: BitLocker
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/bitlocker/get-bitlockervolume?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-BitLockerVolume
---

# Get-BitLockerVolume

## 摘要
获取有关BitLocker可以保护的卷的信息。

## 语法

```
Get-BitLockerVolume [[-MountPoint] <String[]>] [<CommonParameters>]
```

## 描述
**Get-BitLockerVolume** cmdlet 可以获取有关可以被 BitLocker 驱动器加密保护的卷的信息。您可以通过驱动器字母（后跟冒号，例如 C:、E:）来指定一个 BitLocker 卷。如果您不指定驱动器字母，该 cmdlet 会获取当前计算机上的所有卷信息。

你可以使用这个cmdlet来获取BitLocker卷，以便与其他cmdlet（如**Enable-BitLocker**或**Add-BitLockerKeyProtector**）一起使用。此外，你还可以利用这个cmdlet查看有关BitLocker卷的以下信息：

- VolumeType - Data or Operating System.
- Mount Point - Drive letter.
- CapacityGB - Size of drive.
- MetadataVersion - Returns the FVE metadata version of the volume.
    - 0 - **Unknown** - The operating system is unknown.
    - 1 - **Vista** - Windows Vista format, meaning that the volume was protected with BitLocker on a computer running Windows Vista.
    - 2 - **Win7** - Windows 7 format, meaning that the volume was protected with BitLocker on a computer running Windows 7 or the metadata format was upgraded by using the UpgradeVolume method.
- VolumeStatus - Whether BitLocker currently protects some, all, or none of the data on the volume.
- Encryption Percentage - Percent of the volume protected by BitLocker.
- KeyProtector - Type of key protector or protectors.
- AutoUnlock Enabled - Whether BitLocker uses automatic unlocking for the volume.
- Protection Status - Whether BitLocker currently uses a key protector to encrypt the volume encryption key.
- EncryptionMethod - Indicates the encryption algorithm and key size used on the volume.

有关更多信息，请参阅[BitLocker概述](/windows/security/information-protection/bitlocker/bitlocker-overview)。

有关加密方法的概述，请参阅[GetEncryptionMethod方法](/windows/win32/secprov/getencryptionmethod-win32-encryptablevolume)。

## 示例

### 示例 1：获取所有使用 BitLocker 加密的保护卷
```
PS C:\> Get-BitLockerVolume

VolumeType      Mount CapacityGB VolumeStatus           Encryption KeyProtector              AutoUnlock Protection
                Point                                   Percentage                           Enabled    Status
----------      ----- ---------- ------------           ---------- ------------              ---------- ----------
Data            D:        931.51 EncryptionInProgress   1          {RecoveryPassword, Pas...            Off
Data            E:        928.83 FullyDecrypted         0          {}                                   Off
OperatingSystem C:        232.54 FullyDecrypted         0          {Tpm}                                Off
Data            F:          0.98 FullyDecrypted         0          {}                                   Off
Data            G:          1.70 FullyDecrypted         0          {}                                   Off
```

这个命令可以获取当前计算机上所有的 BitLocker 加密卷信息。

### 示例 2：获取特定的 BitLocker 卷
```
PS C:\> Get-BitLockerVolume -MountPoint "E:"

VolumeType      Mount CapacityGB VolumeStatus           Encryption KeyProtector              AutoUnlock Protection
                Point                                   Percentage                           Enabled    Status
----------      ----- ---------- ------------           ---------- ------------              ---------- ----------
Data            E:        928.83 FullyDecrypted         0          {}                                   Off
```

这个命令用于获取指定的 BitLocker 卷。

### 示例 3：获取特定 BitLocker 卷的所有属性
```
PS C:\> Get-BitLockerVolume -MountPoint C | Format-List
ComputerName         : DESKTOP-XXXXXXX
MountPoint           : C:
EncryptionMethod     : XtsAes128
AutoUnlockEnabled    :
AutoUnlockKeyStored  : False
MetadataVersion      : 2
VolumeStatus         : FullyEncrypted
ProtectionStatus     : On
LockStatus           : Unlocked
EncryptionPercentage : 100
WipePercentage       : 0
VolumeType           : OperatingSystem
CapacityGB           : 218,2344
KeyProtector         : {RecoveryPassword, Tpm}
```

这个命令列出了C驱动器上所有与BitLocker相关的属性。

## 参数

### -MountPoint
指定一个驱动器字母数组。此cmdlet用于获取这些使用BitLocker加密的保护卷。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

请帮我将以下Markdown格式转换为中文：  

### BitLockerVolume[], String[]

## 输出

### BitLockerVolume[]

## 备注

## 相关链接

[Add-BitLockerKeyProtector](./Add-BitLockerKeyProtector.md)

[Enable-BitLocker](./Enable-BitLocker.md)

[Enable-BitLockerAutoUnlock](./Enable-BitLockerAutoUnlock.md)
