---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iisadministration/get-iiscentralcertprovider?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IISCentralCertProvider
---

# Get-IISCentralCertProvider

## 摘要
获取有关 IIS 中心证书存储的信息。

## 语法

```
Get-IISCentralCertProvider [-CertStoreLocation] [-UserName] [-PrivateKeyPassword] [-Enabled]
 [<CommonParameters>]
```

## 描述
`Get-IISCentralCertProvider` cmdlet 可以返回有关 IIS 中心证书存储的信息。中心证书存储功能允许您将所有 IIS 证书集中存储在一个位置（例如文件共享文件夹）中，IIS 服务器会从该集中位置获取所需的证书。这意味着您只需在其中一个位置安装证书即可，无需在每台 IIS 服务器上都单独安装相同的证书。

当不带任何参数调用时，`Get-IISCentralCertProvider` 会返回所有证书存储属性的值。或者，您可以添加一个或多个可选参数，以将返回的数据限制为仅包含指定的属性。例如，以下命令会将返回的数据限制为仅包含 `Enabled` 属性：

`Get-IISCentralCertProvider -Enabled`

## 示例

### 示例 1
```
PS C:\> Get-IISCentralCertProvider
```

此命令会返回有关 IIS 中央证书存储的信息。由于在运行此命令时没有使用任何参数，因此 `Get-IISCentralCertProvider` 会返回所有证书存储属性的相关信息。

### 示例 2
```
PS C:\> Get-IISCentralCertProvider -CertStoreLocation -UserName
```

此命令会返回 IIS 中央证书存储库的两个属性的相关信息：存储库的位置（**CertStoreLocation**）以及用于访问该存储库的用户账户名称（**UserName**）。其他属性的值（例如私钥密码）不会被返回。如果想要获取所有属性的值，在调用 **Get-IISCentralCertProvider** 时请省略所有参数。

## 参数

### -CertStoreLocation
这表示在运行命令时将会返回证书存储的位置。如果在调用 **Get-IISCentralCertProvider** 时没有指定任何参数，那么将返回所有属性值的相应信息。

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

### -Enabled
这表示在运行命令时，会返回中央存储的当前状态（是否已启用）。如果在调用 **Get-IISCentralCertProvider** 时没有指定任何参数，那么将返回所有属性值的详细信息。

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

### -PrivateKeyPassword
这表示在运行该命令时，会返回私钥的密码。如果在调用 **Get-IISCentralCertProvider** 时没有指定任何参数，那么将会返回所有属性值的相关信息。

请注意，密码本身不会显示在屏幕上；相反，您只会看到一串星号（*******）。虽然这无法告诉您私钥的密码是什么，但它确实表明证书存储已配置了私钥密码。如果**PrivateKeyPassword**属性没有返回任何值，那就意味着证书存储没有被分配任何私钥密码。

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

### -UserName
这表示在运行命令时将会返回中央存储的用户账户名称。如果在调用 **Get-IISCentralCertProvider** 时没有指定任何参数，那么将会返回所有属性值的详细信息。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于COMMONPARAMETERS（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Clear-IISCentralCertProvider](./Clear-IISCentralCertProvider.md)

[Disable-IISCentralCertProvider](./Disable-IISCentralCertProvider.md)

[Enable-IISCentralCertProvider](./Enable-IISCentralCertProvider.md)

[Set-IISCentralCertProvider](./Set-IISCentralCertProvider.md)

[设置 IISCentralCertProvider 的凭据](./Set-IISCentralCertProviderCredential.md)

