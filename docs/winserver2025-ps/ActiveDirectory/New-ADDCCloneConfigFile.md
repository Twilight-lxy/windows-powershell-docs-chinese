---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/new-addccloneconfigfile?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-ADDCCloneConfigFile
---

# 新增：ADDCCloneConfigFile

## 摘要
执行克隆域控制器所需的预检操作；如果所有检测都通过，则生成克隆配置文件。

## 语法

### IPv4DynamicSettings（默认值）
```
New-ADDCCloneConfigFile [-CloneComputerName <String>] [-IPv4DNSResolver <String[]>] [-Path <String>]
 [-SiteName <String>] [<CommonParameters>]
```

### 离线执行（Offline Execution）
```
New-ADDCCloneConfigFile [-AlternateWINSServer <String>] [-CloneComputerName <String>] [-IPv4Address <String>]
 [-IPv4DefaultGateway <String>] [-IPv4DNSResolver <String[]>] [-IPv4SubnetMask <String>]
 [-IPv6DNSResolver <String[]>] [-Offline] -Path <String> [-PreferredWINSServer <String>] [-SiteName <String>]
 [-Static] [<CommonParameters>]
```

### IPv4StaticSettings
```
New-ADDCCloneConfigFile [-AlternateWINSServer <String>] [-CloneComputerName <String>] -IPv4Address <String>
 [-IPv4DefaultGateway <String>] -IPv4DNSResolver <String[]> -IPv4SubnetMask <String> [-Path <String>]
 [-PreferredWINSServer <String>] [-SiteName <String>] [-Static] [<CommonParameters>]
```

### IPv6DynamicSettings
```
New-ADDCCloneConfigFile [-CloneComputerName <String>] [-IPv6DNSResolver <String[]>] [-Path <String>]
 [-SiteName <String>] [<CommonParameters>]
```

### IPv6静态配置（IPv6StaticSettings）
```
New-ADDCCloneConfigFile [-CloneComputerName <String>] -IPv6DNSResolver <String[]> [-Path <String>]
 [-SiteName <String>] [-Static] [<CommonParameters>]
```


## 描述
`New-ADDCCloneConfigFile` cmdlet 在本地运行时，会对准备进行克隆的域控制器执行先决条件检查。如果所有先决条件检查都通过，该 cmdlet 会在适当的位置生成一个克隆配置文件（DCCloneConfig.xml）。

这个cmdlet有两种运行模式，具体取决于它在何处执行。当在正在准备克隆的域控制器上运行时，它会执行以下先决条件检查，以确保该域控制器已准备好进行克隆：

- Is the PDC emulator FSMO role hosted on a domain controller running Windows Server 2012?
- Is this computer authorized for domain controller cloning (i.e.
is the computer a member of the Cloneable Domain Controllers group)?
- Are all program and services listed in the output of the Get-ADDCCloningExcludedApplicationList cmdlet captured in CustomDCCloneAllowList.xml?

如果所有前提条件检查都通过，**New-ADDCCloneConfigFile** cmdlet将根据提供的参数值在合适的路径生成一个DCCloneConfig.xml文件。该cmdlet也可以通过远程服务器管理工具（Remote Server Administration Tools）从客户端执行，用于为要克隆的域控制器的离线介质生成DCCloneConfig.xml文件；不过，在这种使用模式下不会执行任何前提条件检查。这种使用方式的目的是为每个克隆操作在离线介质的副本上生成具有特定配置值的DCCloneConfig.xml文件。

## 示例

### 示例 1：创建一个具有静态 IPv4 地址的克隆域控制器
```
PS C:\> New-ADDCCloneConfigFile -Static -IPv4Address "10.0.0.2" -IPv4DNSResolver "10.0.0.1" -IPv4SubnetMask "255.255.255.0" -CloneComputerName "VirtualDC2" -IPv4DefaultGateway "10.0.0.3" -PreferredWINSServer "10.0.0.1" -SiteName "REDMOND"
```

此命令创建了一个名为 VirtualDC2 的克隆域控制器，并为其分配了一个静态 IPv4 地址。

### 示例 2：创建一个具有静态 IPv6 设置的克隆域控制器
```
PS C:\> New-ADDCCloneConfigFile -Static -CloneComputerName "Clone1" -IPv6DNSResolver "FEC0:0:0:FFFF::1"
```

这个命令创建了一个名为“Clone1”的克隆域控制器，并为其设置了静态IPv6地址。

### 示例 3：创建一个具有动态 IPv4 设置的克隆域控制器
```
PS C:\> New-ADDCCloneConfigFile -AlternateWINSServer "10.0.0.3" -CloneComputerName "Clone2"-IPv4DNSResolver "10.0.0.1" -PreferredWINSServer "10.0.0.1"
```

该命令创建一个名为“Clone2”的克隆域控制器，其具有动态IPv4地址设置。

#### 示例 4：创建一个具有动态 IPv6 设置的克隆域控制器
```
PS C:\> New-ADDCCloneConfigFile -IPv6DNSResolver "FEC0:0:0:FFFF::1" -SiteName "REDMOND"
```

此命令创建了一个具有动态IPv6设置的克隆域控制器。

#### 示例 5：创建一个具有静态 IPv4 和 IPv6 设置的克隆域控制器
```
PS C:\> New-ADDCCloneConfigFile -Static -IPv4Address "10.0.0.2" -IPv4DNSResolver "10.0.0.1" -IPv4SubnetMask "255.255.255.0" -Static -IPv6DNSResolver "FEC0:0:0:FFFF::1" -CloneComputerName "Clone2" -PreferredWINSServer "10.0.0.1"
```

此命令创建了一个名为“Clone2”的克隆域控制器，该控制器具有静态IPv4和静态IPv6配置。

### 示例 6：创建一个克隆域控制器，该控制器配置了静态 IPv4 地址和动态 IPv6 地址
```
PS C:\> New-ADDCCloneConfigFile -IPv4Address "10.0.0.2" -IPv4DNSResolver "10.0.0.1" -IPv4SubnetMask "255.255.255.0" -IPv4DefaultGateway "10.0.0.3" -IPv6DNSResolver "FEC0:0:0:FFFF::1"
```

此命令创建了一个名为“Clone2”的克隆域控制器，该控制器具有静态IPv4地址和动态IPv6地址配置。

### 示例 7：创建一个具有动态 IPv4 和静态 IPv6 设置的克隆域控制器
```
PS C:\> New-ADDCCloneConfigFile -Static -IPv6DNSResolver "FEC0:0:0:FFFF::1" -CloneComputerName "Clone1" -PreferredWINSServer "10.0.0.1" -SiteName "REDMOND"
```

此命令创建了一个名为“Clone1”的克隆域控制器，该控制器具有动态IPv4地址和静态IPv6地址配置。

### 示例 8：在指定站点中以离线模式创建一个克隆域控制器
```
PS C:\> New-DCCloneConfig -Offline -CloneComputerName "CloneDC1" -SiteName CONTOSO -Path F:\Windows\NTDS -Force
```

此命令会以离线模式创建一个名为 CloneDC1 的域控制器，该控制器位于名为 CONTOSO 的站点中，并使用动态 IPv4 地址。此外，此命令还使用了 *Force* 参数来强制覆盖指定路径（F:\Windows\NTDS）下之前创建的任何 DCCloneConfig.xml 文件。

## 参数

### -AlternateWINSServer
指定备用 Windows Internet 命名服务（WINS）服务器的名称，以便在首选的 WINS 服务器不可用时由克隆的域控制器使用。

```yaml
Type: String
Parameter Sets: OfflineExecution, IPv4StaticSettings
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CloneComputerName
指定克隆后的域控制器的计算机名称。如果此参数没有被指定为一个长度不超过15个字符且在企业内部唯一的名称，那么将使用以下公式来程序化地生成一个名称：

- The first eight characters of the source domain controller computer name.
For instance, a source computer name of SourceComputer is truncated to a prefix string of SourceCo.
- A unique naming suffix of the format **-CL**nnnn is appended to the prefix string where nnnn is the next available value from 0001-9999 that the primary domain controller (PDC) determines is not currently in use.
For example, if 0047 is the next available number within the allowed range, using the above source computer prefix of SourceCo the derived name to use for the clone computer will be SourceCo-CL0047.

```yaml
Type: String
Parameter Sets: (All)
Aliases: cn

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IPv4Address
指定要分配给克隆的域控制器的互联网协议第4版（IPv4）地址。

```yaml
Type: String
Parameter Sets: OfflineExecution
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

```yaml
Type: String
Parameter Sets: IPv4StaticSettings
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```


### -IPv4DefaultGateway
指定用于克隆的域控制器所使用的默认网关的互联网协议版本4（IPv4）地址。

```yaml
Type: String
Parameter Sets: OfflineExecution, IPv4StaticSettings
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IPv4DNSResolver
指定用于被克隆的域控制器解析名称的DNS服务器的互联网协议版本4（IPv4）地址。最多可以提供四个字符串值。

```yaml
Type: String[]
Parameter Sets: IPv4DynamicSettings, OfflineExecution
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

```yaml
Type: String[]
Parameter Sets: IPv4StaticSettings
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IPv4SubnetMask
指定用于克隆后的域控制器所在子网的互联网协议版本4（IPv4）子网掩码。

```yaml
Type: String
Parameter Sets: OfflineExecution
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

```yaml
Type: String
Parameter Sets: IPv4StaticSettings
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IPv6DNSResolver
指定用于被克隆的域控制器解析名称的DNS服务器的互联网协议版本6（IPv6）地址。

```yaml
Type: String[]
Parameter Sets: OfflineExecution, IPv6DynamicSettings
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

```yaml
Type: String[]
Parameter Sets: IPv6StaticSettings
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Offline
用于指示该cmdlet是针对离线媒体运行的，还是针对正在准备克隆的域控制器运行的。

```yaml
Type: SwitchParameter
Parameter Sets: OfflineExecution
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
指定用于编写克隆配置文件的文件夹路径。如果运行该cmdlet且所有前提条件检查均通过，则会生成一个名为DCCloneConfig.xml的文件，并将其作为输出结果保存在该路径下。当在准备进行克隆的域控制器上运行该cmdlet时，*Path*参数是可选的；此时系统会使用DIT文件夹的默认位置，因此无需指定该参数。然而，当以离线模式（即指定了*Offline*参数）运行**New-ADCCLoneConfigFile** cmdlet时，则必须提供*Path*参数。

```yaml
Type: String
Parameter Sets: IPv4DynamicSettings, IPv4StaticSettings, IPv6DynamicSettings, IPv6StaticSettings
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

```yaml
Type: String
Parameter Sets: OfflineExecution
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PreferredWINSServer
指定要使用的主要 Windows Internet 命名服务（WINS）服务器的名称，该服务器将作为克隆域控制器的首选 WINS 服务器。

```yaml
Type: String
Parameter Sets: OfflineExecution, IPv4StaticSettings
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SiteName
指定用于放置克隆域控制器的 Active Directory 站点的名称。

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

### -Static
该参数用于指示为克隆的域控制器指定的TCP/IP配置是静态IP配置还是动态IP配置。

```yaml
Type: SwitchParameter
Parameter Sets: OfflineExecution
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

```yaml
Type: SwitchParameter
Parameter Sets: IPv4StaticSettings, IPv6StaticSettings
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

[Get-ADDCCloningExcludedApplicationList](./Get-ADDCCloningExcludedApplicationList.md)

[Windows PowerShell 中的 AD DS 管理命令集](./activedirectory.md)

