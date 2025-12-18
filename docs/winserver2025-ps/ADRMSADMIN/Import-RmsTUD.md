---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.RightsManagementServices.Admin.dll-Help.xml
Module Name: ADRMSADMIN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adrmsadmin/import-rmstud?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Import-RmsTUD
---

# 导入RmsTUD

## 摘要
从 AD RMS 文件中导入一个 TUD（信任声明），或指定要信任某些 Microsoft 账户 ID。

## 语法

### EnterpriseTUD（默认设置）
```
Import-RmsTUD [-DisplayName] <String> [-SourceFile] <String> [-TrustADFederatedUser] [-PassThru]
 [-Path] <String[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

### WindowsLiveID
```
Import-RmsTUD [-WindowsLiveId] [-PassThru] [-Path] <String[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Import-RmsTUD` cmdlet 用于从 Active Directory Rights Management Services (AD RMS) 中的文件导入企业受信任用户域（TUD），或者指定要信任某个 Microsoft 账户 ID。

要导入企业级TUD（Trusted User Domain）配置文件，请指定*DisplayName*和*SourceFile*参数，并将*Path*参数设置为AD RMS提供程序驱动器文件夹`<PSDrive>:\TrustPolicy\TrustedUserDomain`，其中`<PSDrive>`表示提供程序驱动器的ID。

要信任一个微软账户 ID，请指定 *WindowsLiveID* 参数，并将 *Path* 参数设置为 AD RMS 提供程序的驱动器文件夹 `<PSDrive>:\TrustPolicy\TrustedUserDomain>`。

## 示例

### 示例 1：导入一个 TUD 并为其分配一个名称
```
PS C:\> Import-TUD -Path "." -DisplayName "Fabrikam" -SourceFile "c:\transfer\fabrikam.xml"
```

此命令导入存储在指定文件中的TUD信息，并将名称“Fabrikam”分配给该TUD。

### 示例 2：配置 TUD 以信任微软账户 ID
```
PS C:\> Import-RmsTUD -Path "." -WindowsLiveId
```

此命令配置AD RMS集群以信任Microsoft账户ID。

## 参数

### -Confirm
在运行cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisplayName
指定用于识别正在导入的域的名称。

```yaml
Type: String
Parameter Sets: EnterpriseTUD
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Path
指定提供商提供的驱动器路径或当前驱动器上的相对路径。此参数是必需的。使用点（.）来表示当前位置。该参数不支持通配符，且没有默认值。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SourceFile
指定包含要导入的域名信息的文件的路径。

```yaml
Type: String
Parameter Sets: EnterpriseTUD
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -TrustADFederatedUser
指定要信任 Active Directory Federation Services (ADFS) 的用户。

```yaml
Type: SwitchParameter
Parameter Sets: EnterpriseTUD
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WindowsLiveId
表示可以信任微软账户ID。

```yaml
Type: SwitchParameter
Parameter Sets: WindowsLiveID
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.RightsManagementServices.PowerShell.TrustedUserDomainImportedItem

## 备注

## 相关链接

[使用 Windows PowerShell 与 AD RMS](https://go.microsoft.com/fwlink/?LinkId=136806)

[Export-RmsTUD](./Export-RmsTUD.md)

