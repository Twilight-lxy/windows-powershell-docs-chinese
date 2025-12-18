---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.RightsManagementServices.Admin.dll-Help.xml
Module Name: ADRMSADMIN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adrmsadmin/get-rmssvcaccount?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-RmsSvcAccount
---

# Get-RmsSvcAccount

## 摘要
获取用于 Active Directory 权限管理服务（AD RMS）集群的服务账户凭据。

## 语法

```
Get-RmsSvcAccount [-Path] <String[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Get-RmsSvcAccount` cmdlet 可以获取 Active Directory 权限管理服务（AD RMS）集群的服务账户凭据。

要获取服务账户凭据，请将 *Path* 参数设置为 `<PSDrive>:\`，其中 `<PSDrive>` 是与 AD RMS 集群关联的提供者驱动器的驱动器 ID。

## 示例

### 示例 1：获取服务账户
```
PS C:\> Get-RmsSvcAccount -Path "."
```

此命令显示AD RMS服务账户的信息。

## 参数

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

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

### -Path
指定一个提供程序驱动器及其路径，或者当前驱动器上的相对路径。可以使用点（.）来表示当前位置。此参数不支持通配符，也没有默认值。

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

### -WhatIf
展示了如果该cmdlet被运行会发生的结果。但实际上这个cmdlet并没有被运行。

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

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### System.Management.Automation.PSCredential

## 备注

## 相关链接

[使用 Windows PowerShell 与 AD RMS](https://go.microsoft.com/fwlink/?LinkId=136806)

[Set-RmsSvcAccount](./Set-RmsSvcAccount.md)

