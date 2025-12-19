---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: HgsServer-help.xml
Module Name: HgsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsserver/install-hgsserver?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Install-HgsServer
---

# 安装 HGS 服务器

## 摘要
安装Host Guardian服务服务器。

## 语法

### PrimaryServer_HgsDomain（默认值）
```
Install-HgsServer [-HgsDomainName] <String> -SafeModeAdministratorPassword <SecureString> [-Restart]
 [-LogDirectory <String>] [-DatabasePath <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### AdditionalServer
```
Install-HgsServer [-HgsDomainName] <String> [-HgsDomainCredential] <PSCredential>
 -SafeModeAdministratorPassword <SecureString> [-Restart] [-LogDirectory <String>] [-DatabasePath <String>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Install-HgsServer` cmdlet 用于配置主机防护服务（Host Guardian Service, HGS）所需的基础设施组件，这些组件在安装后需要重新启动。

当此cmdlet在第一个HGS节点上运行时，该节点会被提升为指定域的主域控制器。当此cmdlet在其他HGS节点上运行时，该节点会被提升为指定域的从属域控制器。

对于通过此cmdlet配置的基础设施组件来说，需要重新启动才能使它们正常运行。

有关场景术语的更多信息，请参阅[安全与保障](https://go.microsoft.com/fwlink/?LinkId=699209)。

## 示例

#### 示例 1：在当前节点上安装 HGS 服务器，并提示输入管理员密码
```
PS C:\> Install-HgsServer -HgsDomainName "Contoso.com" -SafeModeAdministratorPassword $SecureStringPassword
```

此命令会在当前节点上安装 HGS 服务器，并将其配置为主服务器。

### 示例 2：在当前节点上安装 HGS 服务器作为安全服务器，并提示输入管理员密码
```
PS C:\> $Credential = Get-Credential
PS C:\> Install-HgsServer -HgsDomainName "Contoso.com" -SafeModeAdministratorPassword $SecureStringPassword -HgsDomainCredential $Credential
```

此命令用于安装HGS服务器，并将当前节点用作安全服务器。

## 参数

### -DatabasePath
指定一个数据库路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HgsDomainCredential
指定用于主HGS服务器的Active Directory域管理员凭据。

```yaml
Type: PSCredential
Parameter Sets: AdditionalServer
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HgsDomainName
指定用于 HGS 服务器的 Active Directory 域的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LogDirectory
指定输出日志目录的位置。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Restart
表示在运行此命令后，系统将会重新启动。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SafeModeAdministratorPassword
当计算机在安全模式（或安全模式的变体，例如目录服务恢复模式）下启动时，该选项用于指定管理员账户的密码。

```yaml
Type: SecureString
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于COMMONParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

## 输出

## 备注

## 相关链接

[HGS 服务器命令行工具](./hgsserver.md)

