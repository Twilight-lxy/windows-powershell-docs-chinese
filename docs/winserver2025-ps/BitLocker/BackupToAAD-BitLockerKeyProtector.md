---
external help file: BitLocker-help.xml
Module Name: bitlocker
schema: 2.0.0
---

# 备份到AAD-BitLocker密钥保护器

## 摘要
在 Microsoft Entra ID 中为 BitLocker 卷保存一个密钥保护器。

## 语法

```
BackupToAAD-BitLockerKeyProtector [-MountPoint] <String[]> [-KeyProtectorId] <String> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`BackupToAAD-BitLockerKeyProtector` cmdlet 用于将受 BitLocker 驱动器加密保护的卷的恢复密码密钥保护器保存到 Microsoft Entra ID。需要通过 ID 指定要保存的密钥。

## 示例

### 示例 1
```powershell
PS C:\> $BLV = Get-BitLockerVolume -MountPoint "C:"
PS C:\> BackupToAAD-BitLockerKeyProtector -MountPoint "C:" -KeyProtectorId $BLV.KeyProtector[1].KeyProtectorId

```

这个示例为指定的 BitLocker 卷保存了一个密钥保护器。

第一个命令使用 **Get-BitLockerVolume** 来获取一个 BitLocker 加密卷，并将其存储在 `$BLV` 变量中。

第二个命令用于备份由 `MountPoint` 参数指定的 BitLocker 卷的密钥保护器。该命令通过使用密钥保护器的 ID 来定位它，这个 ID 存储在 `$BLV` 中的 BitLocker 对象中。

### 示例 2
```powershell
PS C:\> BackupToAAD-BitLockerKeyProtector -MountPoint "C:" -KeyProtectorId "{E2611001E-6AD0-4A08-BAAA-C9c031DB2AA6}"
```
此命令将指定的 BitLocker 卷对应的密钥保护器保存到 Microsoft Entra ID 中。该命令通过使用密钥保护器的 ID 来指定它。

## 参数

### -KeyProtectorId
`KeyProtector` 属性包含一组与卷关联的密钥保护器。该命令使用标准的数组语法来索引 `KeyProtector` 对象。可以通过 `KeyProtector` 对象中的 `KeyProtectorType` 属性来识别对应于恢复密码密钥保护器的那个密钥保护器。


```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -MountPoint
**KeyProtector** 将使用的卷空间大小。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行会发生什么情况。但实际上，这个cmdlet并没有被运行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### System.String

## 输出

### System.Object
## 备注

## 相关链接
