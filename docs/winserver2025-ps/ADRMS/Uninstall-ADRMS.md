---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.RightsManagementServices.Configuration.dll-Help.xml
Module Name: ADRMS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adrms/uninstall-adrms?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Uninstall-ADRMS
---

# 卸载 ADRMS

## 摘要
删除现有 AD RMS 服务器部署的配置信息。

## 语法

```
Uninstall-ADRMS [-ADFSOnly] [-Credential <PSCredential>] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Uninstall-ADRMS` cmdlet 用于删除 Active Directory Rights Management Services (AD RMS) 服务器角色的相关配置，以及随 AD RMS 安装的角色服务（如果适用的话）。如果仅需要删除与身份联合支持（Identity Federation Support）相关的配置，请指定 `ADFSOnly` 参数。

## 示例

### 示例 1：删除 AD RMS 配置
```
PS C:\> Uninstall-ADRMS -Force
```

此命令会删除该计算机上的 AD RMS 配置。有关如何使用此 cmdlet 的更多信息，请参阅 [使用 Windows PowerShell 与 AD RMS](https://go.microsoft.com/fwlink/?LinkId=136806)。

### 示例 2：移除身份联合（Identity Federation）支持配置
```
PS C:\> Uninstall-ADRMS -ADFSOnly -Force
```

此命令会删除该计算机上的身份联合（Identity Federation）支持配置。

## 参数

### -ADFSOnly
从这台计算机上移除对 Active Directory Federation Services (AD FS) 的配置支持，但不会更改 AD RMS 的其他配置设置。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
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
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定用于配置过程的用户凭据。如果指定了此参数，系统会提示您输入凭据。该参数的用法类似于“RunAs”命令。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
通过覆盖那些会阻止命令成功执行的限制来强制完成该命令（只要所做的更改不会危及安全性）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### SwitchParameter

### PSCredential

## 输出

## 备注
* To totally remove the AD RMS role from the system, the **Remove-WindowsFeature** cmdlet must be run after this cmdlet is used. The command to do so is the `Remove-WindowsFeature ADRMS -IncludeManagementTools` command.

## 相关链接

[安装 ADRMS](./Install-ADRMS.md)

[更新-ADRMS](./Update-ADRMS.md)

