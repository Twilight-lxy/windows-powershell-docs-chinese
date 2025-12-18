---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.RightsManagementServices.Admin.dll-Help.xml
Module Name: ADRMSADMIN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adrmsadmin/set-rmssvcaccount?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-RmsSvcAccount
---

# Set-RmsSvcAccount

## 摘要
为 AD RMS 集群设置服务账户。

## 语法

```
Set-RmsSvcAccount [-Credential] <PSCredential> [-Force] [-PassThru] [-Path] <String[]> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-RmsSvcAccount` cmdlet 用于设置 Active Directory 权限管理服务（AD RMS）集群的服务账户。

要指定服务账户，请将 *Credential* 参数设置为该服务账户的凭据，然后将 *Path* 参数设置为 `<PSDrive>:\`，其中 `<PSDrive>` 是 AD RMS 提供者的驱动器 ID。

## 示例

### 示例 1：修改服务账户
```
PS C:\> Set-RmsSvcAccount -Path "."
```

此命令用于更改 AD RMS 服务账户。由于未使用 `Credential` 参数，`Set-RmsSvcAccount` cmdlet 会提示用户输入新服务账户的用户名和密码。

### 示例 2：使用指定的凭据修改服务账户
```
PS C:\> Set-RmsSvcAccount -Path "." -Force -PassThru -Credential ITDOMAIN\adrmssvc
```

此命令用于更改 AD RMS 服务账户。由于 `Credential` 参数指定了该账户的域名和用户名，因此 `Set-RmsSvcAccount` cmdlet 会提示用户输入新服务账户的密码。

### 示例 3：获取用于修改服务账户的凭据
```
PS C:\> $userAccount = Get-Credential ITDOMAIN\adrmssvc
PS C:\> Set-RmsSvcAccount -Path "." -Force -PassThru -Credential $userAccount
```

此命令使用 **Get-Credential** cmdlet 来提示用户输入 ITDOMAIN\adrmsvc 账户的密码，然后将账户凭据安全地存储在一个变量中，之后将该变量传递给 **Set-RmsSvcAccount** cmdlet。

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

### -Credential
指定一个用户名和密码作为 **PSCredential** 对象。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
如果这些限制不会危及安全性，那么可以忽略那些阻止命令成功执行的限制。

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

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此 cmdlet 不会生成任何输出。

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
指定一个提供者驱动器及其路径，或者当前驱动器上的相对路径。可以使用点（.）来表示当前位置。此参数不支持通配符，且没有默认值。

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
展示了如果该cmdlet运行会发生的结果。但实际上该cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### PSCredential

## 备注

## 相关链接

[使用 Windows PowerShell 与 AD RMS](https://go.microsoft.com/fwlink/?LinkId=136806)

[Get-RmsSvcAccount](./Get-RmsSvcAccount.md)

